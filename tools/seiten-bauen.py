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

# Wo die Seite auf dem Server liegt. In der Vorschau unter
# kodozen.github.io/ckr/ ist das "/ckr/", auf der echten Domain "/".
# Gebraucht wird das nur von der 404-Seite: sie wird für JEDE unbekannte
# Adresse ausgeliefert, auch für /a/b/c/ — relative Pfade zeigen von dort
# ins Leere. Sie ist deshalb die einzige Seite mit absoluten Verweisen.
SEITEN_WURZEL = os.environ.get("SEITEN_WURZEL", "/")

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
    s = re.sub(r'\b(href|src|srcset)="(?!https?:|#|/|mailto:|tel:|data:|\./|\.\./)([^"]+)"',
               lambda m: '%s="../%s"' % (m.group(1), m.group(2)), s)
    # Ankersprünge zeigen auf die Startseite, nicht auf diese Seite
    s = re.sub(r'href="#([a-z-]+)"', r'href="../#\1"', s)
    s = s.replace('href="/"', 'href="../"')
    s = s.replace('href="./"', 'href="../"')
    return s


def teile_holen():
    """Kopf, Fuß und den gemeinsamen Kopfblock aus index.html schneiden.

    Nichts davon wird abgeschrieben. Ändert sich in index.html das Menü,
    ein Symbol oder das Vorschaubild, ändert es sich beim nächsten Lauf
    auf allen sechzehn Seiten mit."""
    quelle = lies("index.html")
    kopf = re.search(r'<header class="kopf".*?</header>', quelle, re.S).group(0)
    fuss = re.search(r'<footer class="fuss".*?</footer>', quelle, re.S).group(0)
    gemeinsam = re.search(r'<!-- kopf:gemeinsam.*?<!-- /kopf:gemeinsam -->',
                          quelle, re.S).group(0)
    return tiefer(kopf), tiefer(fuss), tiefer(gemeinsam)


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
<link rel="stylesheet" href="../schriften.css?v=23">
<link rel="stylesheet" href="../styles.css?v=23">
<script src="../app.js?v=23" defer></script>

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


def daten_einfach(p):
    """WebPage und Brotkrume für Impressum, Datenschutz, Bewerbung.

    Ohne das versteht eine Suchmaschine zwar den Text, aber nicht, wo
    die Seite im Haus steht. Die Brotkrume ist außerdem das, was in der
    Trefferliste statt der nackten Adresse angezeigt wird."""
    seite = "%s/%s/" % (BASIS, p["slug"])
    return json.dumps({
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": seite, "name": p["titel"],
             "description": p["beschreibung"], "url": seite,
             "inLanguage": "de-AT",
             "isPartOf": {"@id": BASIS + "/#website"},
             "publisher": {"@id": BASIS + "/#betrieb"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Startseite",
                 "item": BASIS + "/"},
                {"@type": "ListItem", "position": 2, "name": p["titel"],
                 "item": seite}]},
        ]}, ensure_ascii=False, indent=1)


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
<link rel="stylesheet" href="../schriften.css?v=23">
<link rel="stylesheet" href="../styles.css?v=23">
<script src="../app.js?v=23" defer></script>

%(regeln)s

<script type="application/ld+json">
%(daten)s
</script>
</head>
<body>

<a class="skip" href="#inhalt">Zum Inhalt springen</a>

%(kopf)s

<main id="inhalt" class="rechtsseite">
  <nav class="krume" aria-label="Sie sind hier">
    <div class="huelle">
      <ol>
        <li><a href="../">Start</a></li>
        <li aria-current="page">%(titel)s</li>
      </ol>
    </div>
  </nav>
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
        "daten": daten_einfach(p),
    }


# ----------------------------------------------------------------------
# 404
# ----------------------------------------------------------------------
# Eigenständig, ohne eine einzige externe Datei. Der Grund: diese Seite
# wird für jede unbekannte Adresse ausgeliefert — auch für /a/b/c/xyz.
# Läge das Stylesheet relativ daneben, würde es von dort mitfehlschlagen
# und der Besucher bekäme unformatierten Text zu sehen. Eine Fehlerseite,
# die selbst kaputt aussieht, ist schlimmer als gar keine.

def vierhundertvier(p):
    w = SEITEN_WURZEL
    rumpf = p["rumpf"].replace('href="', 'href="%s' % w)
    rumpf = rumpf.replace('href="%stel:' % w, 'href="tel:')
    rumpf = rumpf.replace('href="%s#' % w, 'href="%s#' % w)
    return """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titel)s · %(firma)s</title>
<meta name="description" content="%(beschreibung)s">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#141446">
<link rel="icon" href="%(wurzel)sfavicon.ico" sizes="any">
<link rel="apple-touch-icon" href="%(wurzel)sapple-touch-icon.png">

<!-- Alles inline: diese Seite muss auch dann vollständig aussehen,
     wenn sie unter einer beliebig tiefen Adresse ausgeliefert wird. -->
<style>
:root {
  --grund:#F7F8FB; --flaeche:#fff; --tinte:#141446; --tinte-weich:#4A4A72;
  --linie:#E2E5EE; --blau:#2838C8; --gruen:#3E9E14;
}
* { box-sizing:border-box; }
body {
  margin:0; background:var(--grund); color:var(--tinte);
  font:16px/1.6 system-ui, "Segoe UI", sans-serif;
  -webkit-font-smoothing:antialiased;
}
.huelle { max-width:46rem; margin:0 auto; padding:clamp(2rem,7vw,4.5rem) clamp(1rem,4vw,2.4rem); }
h1 { font-size:clamp(2rem,1.4rem + 2.9vw,3.2rem); line-height:1.08; margin:0 0 1rem;
     letter-spacing:-0.02em; }
h2 { font-size:1.2rem; margin:2.4rem 0 0.8rem; padding-top:1.2rem;
     border-top:1px solid var(--linie); }
p { margin:0 0 1rem; }
a { color:var(--blau); }
.marker { font-size:0.85rem; font-weight:600; letter-spacing:0.04em;
          text-transform:uppercase; color:var(--gruen); margin:0 0 0.5rem; }
.vorspann { font-size:1.15rem; color:var(--tinte-weich); max-width:46ch; }
.vierkant { list-style:none; margin:0; padding:0;
            display:grid; gap:0.5rem;
            grid-template-columns:repeat(auto-fit,minmax(14rem,1fr)); }
.vierkant a {
  display:flex; align-items:center; min-height:46px;
  padding:0.5rem 0.9rem; border:1px solid var(--linie); border-radius:10px;
  background:var(--flaeche); color:inherit; text-decoration:none;
}
.vierkant a:hover { border-color:var(--gruen); color:var(--blau); }
.knoepfe { display:flex; flex-wrap:wrap; gap:0.7rem; margin-top:1.4rem; }
.knopf {
  display:inline-flex; align-items:center; gap:0.4rem; min-height:46px;
  padding:0.6rem 1.2rem; border-radius:10px; text-decoration:none;
  border:1px solid var(--tinte); color:var(--tinte); font-weight:600;
}
.knopf--voll { background:var(--tinte); color:#fff; }
:focus-visible { outline:3px solid var(--blau); outline-offset:2px; }
</style>
</head>
<body>
<main class="huelle">
%(rumpf)s
</main>
</body>
</html>
""" % {
        "titel": a(p["titel"]),
        "firma": FIRMA,
        "beschreibung": a(p["beschreibung"]),
        "wurzel": w,
        "rumpf": rumpf.replace('class="abschnitt__vorspann"', 'class="vorspann"')
                      .replace('class="rechtsseite__knoepfe"', 'class="knoepfe"'),
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
        if p.get("datei"):
            ziel = os.path.join(WURZEL, p["datei"])
            with open(ziel, "w", encoding="utf-8") as f:
                f.write(vierhundertvier(p))
            print("  %-32s %5.1f KB" % (p["datei"], os.path.getsize(ziel) / 1024))
            continue
        ordner = os.path.join(WURZEL, p["slug"])
        os.makedirs(ordner, exist_ok=True)
        ziel = os.path.join(ordner, "index.html")
        with open(ziel, "w", encoding="utf-8") as f:
            f.write(einfache_seite(p, kopf, fuss))
        print("  %-32s %5.1f KB" % (p["slug"] + "/", os.path.getsize(ziel) / 1024))
    print("%d einfache Seiten gebaut." % len(SEITEN))


if __name__ == "__main__":
    main()
