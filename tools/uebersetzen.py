#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt eine übersetzte Fassung der Startseite.

Quelle ist immer die deutsche index.html. Jede Sprache hat eine
Wörterbuchdatei i18n/<code>.json, in der links der deutsche Satz und
rechts die Übersetzung steht — dieselbe Datei dient damit auch als
Korrekturvorlage.

    python3 tools/uebersetzen.py tr

Türkisch ist nur für die interne Abnahme gedacht; die erzeugte Seite
bekommt deshalb noindex und taucht im Sprachumschalter nicht auf.
"""
import json, os, re, sys, html

INTERN = {"tr"}          # Sprachen, die nicht in den Index sollen
LOCALE = {"tr": "tr_TR", "en": "en_US", "de": "de_AT"}


def uebersetzen(quelle, woerter, code):
    s = quelle
    fehlend = []

    def wort(t):
        t2 = re.sub(r"\s+", " ", t).strip()
        if not t2 or t2.isdigit():
            return None
        if t2 in woerter:
            return woerter[t2]
        # Nur echte Sätze melden, keine Zahlen oder Zeichen
        if len(t2) > 2 and re.search(r"[A-Za-zÄÖÜäöüß]", t2):
            fehlend.append(t2)
        return None

    # --- Textknoten. Skripte, Stile und Kommentare bleiben unberührt.
    schutz = []

    def parken(m):
        schutz.append(m.group(0))
        return "\x00%d\x00" % (len(schutz) - 1)

    s = re.sub(r"<!--.*?-->", parken, s, flags=re.S)
    # Nur eingebettete Skripte parken. Ein <script src="…"> hat keinen
    # Text, muss aber seinen Pfad angepasst bekommen — wird es geparkt,
    # bleibt der Pfad stehen und die Datei fehlt in der Unterseite.
    s = re.sub(r"<script(?![^>]*\bsrc=)[^>]*>.*?</script>", parken, s, flags=re.S)
    s = re.sub(r"<style[^>]*>.*?</style>", parken, s, flags=re.S)

    def knoten(m):
        roh = m.group(1)
        neu = wort(html.unescape(roh))
        if neu is None:
            return m.group(0)
        # Einrückung des Originals beibehalten
        vorn = re.match(r"\s*", roh).group(0)
        hint = re.search(r"\s*$", roh).group(0)
        return ">" + vorn + html.escape(neu, quote=False) + hint + "<"

    s = re.sub(r">([^<>]+)<", knoten, s)

    # --- Übersetzbare Attribute
    for oz in ("alt", "aria-label", "content"):
        def attribut(m, oz=oz):
            neu = wort(html.unescape(m.group(1)))
            if neu is None:
                return m.group(0)
            return '%s="%s"' % (oz, html.escape(neu, quote=True))
        s = re.sub(r'%s="([^"]*)"' % oz, attribut, s)

    s = re.sub(r"<title>([^<]*)</title>",
               lambda m: "<title>%s</title>" % html.escape(wort(html.unescape(m.group(1))) or m.group(1), quote=False),
               s, count=1)

    # --- Kopf anpassen
    s = s.replace('<html lang="de">', '<html lang="%s">' % code, 1)
    s = re.sub(r'<meta property="og:locale" content="[^"]*">',
               '<meta property="og:locale" content="%s">' % LOCALE.get(code, code), s, count=1)

    # Pfade gehen eine Ebene tiefer
    s = re.sub(r'\b(href|src|srcset)="(?!https?:|#|/|mailto:|tel:|data:|\./)([^"]+)"',
               lambda m: '%s="../%s"' % (m.group(1), m.group(2)), s)
    # "./" zeigt auf die Startseite; eine Ebene tiefer ist das "../"
    s = s.replace('href="./"', 'href="../"')

    # Die Leistungsliste im Formular kommt aus app.js, nicht aus dem
    # HTML — sonst bliebe sie in der übersetzten Fassung deutsch und
    # wäre bei der Abnahme nicht prüfbar. Die übersetzten Namen werden
    # hier eingesetzt; app.js nimmt sie, wenn sie da sind.
    aus_js = [
        "Unterhaltsreinigung", "Treppenhausreinigung", "Grundreinigung",
        "Allgemeine Raumpflege", "Büro- und Privatreinigung", "Glasreinigung",
        "Fenster- & Fassadenreinigung", "Dachreinigung", "Solaranlagenreinigung",
        "Hotelreinigung", "Appartementreinigung", "Werkstattreinigung",
        "Baureinigung & Endreinigung", "Entrümpelung & Hausbetreuung",
        "Teppichreinigung", "Verkehrsmittelreinigung", "Denkmalreinigung"
    ]
    uebersetzt = [woerter.get(n, n) for n in aus_js]
    einschub = ('<script>window.CKR_LEISTUNGEN = %s;</script>'
                % json.dumps(uebersetzt, ensure_ascii=False))
    s = s.replace("</head>", einschub + "\n</head>", 1)

    if code in INTERN:
        s = s.replace("<head>",
                      "<head>\n<!-- Interne Abnahmefassung: nicht für Besucher, nicht für Suchmaschinen. -->\n"
                      '<meta name="robots" content="noindex, nofollow">', 1)

    for i, teil in enumerate(schutz):
        s = s.replace("\x00%d\x00" % i, teil)
    return s, fehlend


def main(code):
    kok = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    quelle = open(os.path.join(kok, "index.html"), encoding="utf-8").read()
    woerter = json.load(open(os.path.join(kok, "i18n", code + ".json"), encoding="utf-8"))
    woerter = {k: v for k, v in woerter.items() if not k.startswith("_")}

    s, fehlend = uebersetzen(quelle, woerter, code)
    ziel = os.path.join(kok, code)
    os.makedirs(ziel, exist_ok=True)
    open(os.path.join(ziel, "index.html"), "w", encoding="utf-8").write(s)

    print("%s/index.html geschrieben — %d Einträge im Wörterbuch" % (code, len(woerter)))
    eindeutig = []
    for t in fehlend:
        if t not in eindeutig:
            eindeutig.append(t)
    if eindeutig:
        print("\nnoch ohne Übersetzung (%d):" % len(eindeutig))
        for t in eindeutig:
            print("  ·", t[:100])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "tr"))
