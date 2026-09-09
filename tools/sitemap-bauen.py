#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Schreibt sitemap.xml und robots.txt.

Ohne Sitemap findet eine Suchmaschine neue Unterseiten irgendwann von
allein — mit Sitemap sofort und vollständig. Bei dreizehn frischen
Adressen, die es vorher nicht gab, ist das der Unterschied zwischen
„nächste Woche“ und „nächstes Quartal“.

Seiten mit noindex kommen nicht hinein: eine Adresse anzumelden und
gleichzeitig auszusperren ist ein Widerspruch, den Google meldet.
"""
import datetime
import os
import sys

WURZEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, os.path.join(WURZEL, "inhalt"))
from leistungen import LEISTUNGEN     # noqa: E402
from seiten import SEITEN             # noqa: E402

BASIS = "https://www.ckrreinigung.at"
HEUTE = datetime.date.today().isoformat()


def main():
    eintraege = [("/", "1.0")]
    eintraege += [("/%s/" % l["slug"], "0.8") for l in LEISTUNGEN]
    eintraege += [("/%s/" % p["slug"], "0.4")
                  for p in SEITEN if not p.get("noindex")]

    zeilen = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for pfad, gewicht in eintraege:
        zeilen += ["  <url>",
                   "    <loc>%s%s</loc>" % (BASIS, pfad),
                   "    <lastmod>%s</lastmod>" % HEUTE,
                   "    <priority>%s</priority>" % gewicht,
                   "  </url>"]
    zeilen.append("</urlset>")
    with open(os.path.join(WURZEL, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(zeilen) + "\n")

    robots = """# CKR Cleaning Services
# Erzeugt von tools/sitemap-bauen.py

User-agent: *
Allow: /

# Die türkische Fassung ist nur für die interne Abnahme gedacht.
Disallow: /tr/
# Werkzeugseite, gehört nicht zur Website.
Disallow: /video-pruefen.html

Sitemap: %s/sitemap.xml
""" % BASIS
    with open(os.path.join(WURZEL, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    print("sitemap.xml — %d Adressen" % len(eintraege))
    print("robots.txt geschrieben")


if __name__ == "__main__":
    main()
