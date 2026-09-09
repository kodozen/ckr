#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Baut die Leistungsseiten aus inhalt/leistungen.py.

    python3 tools/seiten-bauen.py

Kopf und Fuß werden aus index.html gelesen, nicht abgeschrieben. Ändert
sich dort die Telefonnummer oder ein Menüpunkt, ändert sich beim nächsten
Lauf jede Unterseite mit. Dreizehn handgepflegte Dateien driften
auseinander; eine Vorlage tut das nicht.

Die Adressen sind dieselben wie auf der alten Website. Der Domainname
bleibt — wer die alten Adressen wegwirft, wirft jede Google-Platzierung
und jeden fremden Link mit weg.
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "inhalt"))
from leistungen import LEISTUNGEN, NACH_SLUG          # noqa: E402
from seiten import SEITEN                             # noqa: E402

WURZEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASIS = "https://www.ckrreinigung.at"
FIRMA = "CKR Cleaning Services"
TELEFON = "+436508933881"
TELEFON_LESBAR = "+43 650 893 38 81"
EMAIL = "info@ckrreinigung.at"
ORT = "Kufstein"
SYMBOL = ""

# Vorausladen: zeigt jemand rund zwei Zehntelsekunden auf einen Link,
# baut der Browser die Zielseite schon auf. Der Klick wirkt dann nicht
# schnell, sondern sofort. „moderate“ lädt erst bei echter Absicht, nicht
# auf Verdacht — es wird kein Datenvolumen verschwendet.
REGELN = """<script type="speculationrules">
{
  "prerender": [{
    "where": { "and": [
      { "href_matches": "/*" },
      { "not": { "href_matches": "/tr/*" } },
      { "not": { "href_matches": "/video-pruefen.html" } }
    ]},
    "eagerness": "moderate"
  }]
}
</script>"""


def lies(name):
    with open(os.path.join(WURZEL, name), encoding="utf-8") as f:
        return f.read()


def tiefer(s):
    """Relative Pfade eine Ebene tiefer schieben."""
    s = re.sub(r'\b(href|src|srcset)="(?!https?:|#|/|mailto:|tel:|data:|\.\./)([^"]+)"',
               lambda m: '%s="../%s"' % (m.group(1), m.group(2)), s)
    # Ankersprünge zeigen auf die Startseite, nicht auf diese Seite
    s = re.sub(r'href="#([a-z-]+)"', r'href="../#\1"', s)
    s = s.replace('href="/"', 'href="../"')
    return s


def teile_holen():
    """Kopf, Fuß und Tab-Symbol aus index.html schneiden."""
    quelle = lies("index.html")
    kopf = re.search(r'<header class="kopf".*?</header>', quelle, re.S).group(0)
    fuss = re.search(r'<footer class="fuss".*?</footer>', quelle, re.S).group(0)
    symbol = re.search(r'<link rel="icon"[^>]*>', quelle).group(0)
    return tiefer(kopf), tiefer(fuss), symbol


def e(t):
    return html.escape(t, quote=False)


def a(t):
    return html.escape(t, quote=True)


# ----------------------------------------------------------------------
# Strukturierte Daten
# ----------------------------------------------------------------------
# Suchmaschinen lesen die Seite ohnehin. Mit diesen paar Zeilen verstehen
# sie zusätzlich, dass es sich um eine Dienstleistung eines örtlichen
# Betriebs handelt, wo er sitzt und welche Fragen die Seite beantwortet.
# Kostet nichts an Ladezeit und ist der einzige Weg, in der Trefferliste
# mehr als zwei Zeilen Text zu bekommen. Die alte Website hat davon nichts.

def daten_block(l):
    seite = "%s/%s/" % (BASIS, l["slug"])
    dienst = {
        "@type": "Service",
        "@id": seite + "#dienst",
        "name": l["titel"],
        "serviceType": l["titel"],
        "description": l["vorspann"],
        "provider": {"@id": BASIS + "/#betrieb"},
        "areaServed": {"@type": "State", "name": "Tirol"},
    }
    krumen = {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Startseite", "item": BASIS + "/"},
            {"@type": "ListItem", "position": 2, "name": "Leistungen", "item": BASIS + "/#leistungen"},
            {"@type": "ListItem", "position": 3, "name": l["titel"], "item": seite},
        ],
    }
    graph = [dienst, krumen]
    if l.get("fragen"):
        graph.append({
            "@type": "FAQPage",
            "@id": seite + "#fragen",
            "mainEntity": [
                {"@type": "Question", "name": f,
                 "acceptedAnswer": {"@type": "Answer", "text": t}}
                for f, t in l["fragen"]
            ],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, indent=1)


# ----------------------------------------------------------------------
# Vorlage
# ----------------------------------------------------------------------

def seite_bauen(l, kopf, fuss):
    slug = l["slug"]
    titel = "%s in %s · %s" % (l["titel"], ORT, FIRMA)
    beschreibung = l["vorspann"].replace("\n", " ")
    if len(beschreibung) > 155:
        beschreibung = beschreibung[:152].rsplit(" ", 1)[0] + " …"

    kern = "\n".join("        <p>%s</p>" % e(p) for p in l["kern"])
    punkte = "\n".join("          <li>%s</li>" % e(p) for p in l["punkte"])
    warum_titel, warum_text = l["warum"]
    fragen = "\n".join(
        """        <details class="frage">
          <summary>%s</summary>
          <p>%s</p>
        </details>""" % (e(f), e(t)) for f, t in l["fragen"])

    verwandt = "\n".join(
        """          <a class="nachbar" href="../%s/">
            <span class="nachbar__gruppe">%s</span>
            <span class="nachbar__name">%s</span>
            <span class="nachbar__satz">%s</span>
          </a>""" % (v, e(NACH_SLUG[v]["gruppe"]), e(NACH_SLUG[v]["titel"]),
                     e(NACH_SLUG[v]["kurz"]))
        for v in l["verwandt"])

    return """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titel)s</title>
<meta name="description" content="%(beschreibung)s">
<meta name="theme-color" content="#141446">
<link rel="canonical" href="%(basis)s/%(slug)s/">

<meta property="og:type" content="website">
<meta property="og:title" content="%(og_titel)s">
<meta property="og:description" content="%(beschreibung)s">
<meta property="og:url" content="%(basis)s/%(slug)s/">
<meta property="og:locale" content="de_AT">

%(symbol)s
<!-- Schriften vom eigenen Server; siehe tools/schriften-holen.py -->
<link rel="preload" href="../schrift/archivo-700-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="../schrift/public-sans-400-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../schriften.css?v=13">
<link rel="stylesheet" href="../styles.css?v=13">
<script src="../app.js?v=13" defer></script>

%(regeln)s

<!-- Strukturierte Daten: erzeugt von tools/seiten-bauen.py -->
<script type="application/ld+json">
%(daten)s
</script>
</head>
<body>

<a class="skip" href="#inhalt">Zum Inhalt springen</a>

%(kopf)s

<main id="inhalt">

  <nav class="krume" aria-label="Sie sind hier">
    <div class="huelle">
      <ol>
        <li><a href="../">Start</a></li>
        <li><a href="../#leistungen">Leistungen</a></li>
        <li aria-current="page">%(name)s</li>
      </ol>
    </div>
  </nav>

  <section class="lseite__kopf">
    <div class="huelle">
      <p class="marker">%(marker)s</p>
      <h1>%(name)s</h1>
      <p class="vorspann">%(kurz)s</p>
      <p class="lseite__lead">%(vorspann)s</p>
      <div class="auftakt__knoepfe">
        <a class="knopf knopf--voll" href="../#angebot">Angebot anfordern</a>
        <a class="knopf" href="tel:%(tel)s"><span aria-hidden="true">☎</span> %(tel_lesbar)s</a>
      </div>
      <p class="auftakt__notiz">Kostenlose Besichtigung · danach Fixpreis</p>
    </div>
  </section>

  <section class="lseite__kern">
    <div class="huelle lseite__spalten">
      <div class="lseite__text">
%(kern)s
      </div>
      <aside class="lseite__liste">
        <h2>Was dazugehört</h2>
        <ul class="haken">
%(punkte)s
        </ul>
        <p class="lseite__hinweis">
          Nicht vollständig und nicht in Stein — was fehlt, nehmen wir dazu.
        </p>
      </aside>
    </div>
  </section>

  <section class="lseite__warum">
    <div class="huelle">
      <h2>%(warum_titel)s</h2>
      <p>%(warum_text)s</p>
    </div>
  </section>

  <section class="faq lseite__faq" aria-labelledby="f-%(slug)s">
    <div class="huelle">
      <h2 id="f-%(slug)s">Fragen zu %(name)s</h2>
      <div class="faq__liste">
%(fragen)s
      </div>
    </div>
  </section>

  <section class="lseite__weiter">
    <div class="huelle">
      <h2>Passt oft dazu</h2>
      <div class="nachbarn">
%(verwandt)s
      </div>
    </div>
  </section>

  <section class="lseite__ruf">
    <div class="huelle">
      <h2>Sagen Sie uns, worum es geht</h2>
      <p>
        Wir kommen vorbei, sehen es uns an — kostenlos und unverbindlich —
        und nennen danach einen Fixpreis.
      </p>
      <div class="auftakt__knoepfe">
        <a class="knopf knopf--voll" href="../#angebot">Angebot anfordern</a>
        <a class="knopf" href="mailto:%(mail)s">%(mail)s</a>
      </div>
    </div>
  </section>

</main>

%(fuss)s

</body>
</html>
""" % {
        "titel": a(titel),
        "og_titel": a("%s · %s" % (l["titel"], FIRMA)),
        "beschreibung": a(beschreibung),
        "basis": BASIS,
        "slug": slug,
        "daten": daten_block(l),
        "kopf": kopf,
        "fuss": fuss,
        "name": e(l["titel"]),
        "marker": e(l["marker"]),
        "kurz": e(l["kurz"]),
        "vorspann": e(l["vorspann"]),
        "kern": kern,
        "punkte": punkte,
        "warum_titel": e(warum_titel),
        "warum_text": e(warum_text),
        "fragen": fragen,
        "verwandt": verwandt,
        "tel": TELEFON,
        "tel_lesbar": TELEFON_LESBAR,
        "mail": EMAIL,
        "regeln": REGELN,
        "symbol": SYMBOL,
    }


# ----------------------------------------------------------------------
# Einfache Seiten: Impressum, Datenschutz, Bewerbung
# ----------------------------------------------------------------------
# Reiner Lesetext. Sie bekommen dasselbe Gerüst wie alles andere, damit
# der Kopf an einer einzigen Stelle gepflegt wird.

def einfache_seite(p, kopf, fuss):
    noindex = ('<meta name="robots" content="noindex">\n'
               if p.get("noindex") else "")
    return """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titel)s · %(firma)s</title>
<meta name="description" content="%(beschreibung)s">
<meta name="theme-color" content="#141446">
<link rel="canonical" href="%(basis)s/%(slug)s/">
%(noindex)s%(symbol)s
<link rel="preload" href="../schrift/archivo-700-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="../schrift/public-sans-400-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="../schriften.css?v=13">
<link rel="stylesheet" href="../styles.css?v=13">
<script src="../app.js?v=13" defer></script>

%(regeln)s
</head>
<body>

<a class="skip" href="#inhalt">Zum Inhalt springen</a>

%(kopf)s

<main id="inhalt" class="rechtsseite">
  <div class="huelle">
    %(rumpf)s

    <p class="rechtsseite__zurueck"><a class="knopf" href="../">Zurück zur Startseite</a></p>
  </div>
</main>

%(fuss)s

</body>
</html>
""" % {
        "titel": a(p["titel"]),
        "firma": FIRMA,
        "beschreibung": a(p["beschreibung"]),
        "basis": BASIS,
        "slug": p["slug"],
        "noindex": noindex,
        "regeln": REGELN,
        "symbol": SYMBOL,
        "kopf": kopf,
        "fuss": fuss,
        "rumpf": p["rumpf"],
        "symbol": SYMBOL,
    }


def main():
    global SYMBOL
    kopf, fuss, SYMBOL = teile_holen()
    for l in LEISTUNGEN:
        ordner = os.path.join(WURZEL, l["slug"])
        os.makedirs(ordner, exist_ok=True)
        ziel = os.path.join(ordner, "index.html")
        with open(ziel, "w", encoding="utf-8") as f:
            f.write(seite_bauen(l, kopf, fuss))
        print("  %-32s %5.1f KB" % (l["slug"] + "/", os.path.getsize(ziel) / 1024))
    print("%d Leistungsseiten gebaut." % len(LEISTUNGEN))

    for p in SEITEN:
        ordner = os.path.join(WURZEL, p["slug"])
        os.makedirs(ordner, exist_ok=True)
        ziel = os.path.join(ordner, "index.html")
        with open(ziel, "w", encoding="utf-8") as f:
            f.write(einfache_seite(p, kopf, fuss))
        print("  %-32s %5.1f KB" % (p["slug"] + "/", os.path.getsize(ziel) / 1024))
    print("%d einfache Seiten gebaut." % len(SEITEN))


if __name__ == "__main__":
    main()
