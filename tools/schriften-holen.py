#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Holt die Schriftdateien von Google und legt sie lokal ab.

Warum überhaupt: werden Schriften von fonts.googleapis.com geladen,
geht bei jedem Seitenaufruf die IP-Adresse des Besuchers an Google.
In Deutschland gab es dazu Abmahnungen, in Österreich ist die Lage
strittig. Selbst hosten löst das Problem vollständig — und spart
nebenbei zwei DNS-Auflösungen und einen fremden Verbindungsaufbau.

Einmal ausführen, dann liegt alles im Ordner schrift/ und in
schriften.css. Danach nur wieder nötig, wenn eine Schrift oder ein
Schnitt dazukommt.

    python3 tools/schriften-holen.py

Es werden nur die Schnitte geladen, die styles.css wirklich benutzt
(Liste unten) und nur die Subsets latin und latin-ext — latin trägt
Deutsch, latin-ext die türkischen Zeichen der internen Fassung.
"""
import os, re, subprocess, sys

# Genau die Schnitte, die styles.css verwendet. Wer einen neuen
# font-weight einführt, trägt ihn hier nach — sonst rechnet der
# Browser ihn aus dem nächstliegenden hoch und es sieht matt aus.
SCHNITTE = {
    "Archivo": [500, 600, 700],
    "Public Sans": [400, 600],
}
SUBSETS = {"latin", "latin-ext"}
ORDNER = "schrift"
ZIEL_CSS = "schriften.css"

KOPF = """/* ============================================================
   Schriften — selbst gehostet
   ------------------------------------------------------------
   Diese Datei wird von tools/schriften-holen.py erzeugt.
   Nicht von Hand ändern.

   Vorher kamen Archivo und Public Sans von fonts.googleapis.com.
   Dabei geht bei jedem Seitenaufruf die IP-Adresse des Besuchers
   an Google. Die Dateien liegen jetzt unter schrift/; die Seite
   spricht mit keinem fremden Server mehr.

   font-display: swap — der Text ist sofort lesbar und wird
   nachträglich in die richtige Schrift umgesetzt. Ohne das bliebe
   die Seite bis zu drei Sekunden leer.
   ============================================================ */
"""

# Ein Browser-Kennzeichen ist nötig: ohne liefert Google die alten
# TTF-Regeln statt woff2.
BROWSER = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
           "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def holen(url, ziel=None):
    befehl = ["curl", "-sS", "-f", "-m", "40", "-A", BROWSER]
    if ziel:
        befehl += ["-o", ziel, url]
        subprocess.run(befehl, check=True)
        return None
    return subprocess.run(befehl + [url], check=True,
                          capture_output=True, text=True).stdout


def main():
    familien = "&".join(
        "family=%s:wght@%s" % (name.replace(" ", "+"),
                               ";".join(str(g) for g in sorted(gewichte)))
        for name, gewichte in SCHNITTE.items())
    css = holen("https://fonts.googleapis.com/css2?%s&display=swap" % familien)

    os.makedirs(ORDNER, exist_ok=True)
    # Google setzt vor jeden Block einen Kommentar mit dem Subset-Namen.
    teile = re.split(r"/\*\s*([a-z0-9-]+)\s*\*/", css)

    regeln = []
    for i in range(1, len(teile), 2):
        subset, block = teile[i], teile[i + 1]
        if subset not in SUBSETS:
            continue
        familie = re.search(r"font-family:\s*'([^']+)'", block).group(1)
        gewicht = re.search(r"font-weight:\s*(\d+)", block).group(1)
        url = re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1)
        bereich = re.search(r"unicode-range:\s*([^;]+);", block).group(1).strip()

        name = "%s-%s-%s.woff2" % (familie.lower().replace(" ", "-"),
                                   gewicht, subset)
        pfad = os.path.join(ORDNER, name)
        if not os.path.exists(pfad) or os.path.getsize(pfad) == 0:
            holen(url, pfad)
        regeln.append((familie, int(gewicht), subset, name, bereich,
                       os.path.getsize(pfad)))

    if not regeln:
        sys.exit("Keine passenden Schriftschnitte gefunden — Antwort von "
                 "Google unerwartet.")

    regeln.sort(key=lambda r: (r[0], r[1], r[2]))
    stuecke = [KOPF]
    for familie, gewicht, subset, name, bereich, _ in regeln:
        stuecke.append("""@font-face {
  font-family: '%s';
  font-style: normal;
  font-weight: %d;
  font-display: swap;
  src: url('%s/%s') format('woff2');
  unicode-range: %s;
}""" % (familie, gewicht, ORDNER, name, bereich))
    open(ZIEL_CSS, "w", encoding="utf-8").write("\n".join(stuecke) + "\n")

    # Aufräumen: Dateien, die nicht mehr gebraucht werden
    gewollt = {r[3] for r in regeln}
    for datei in sorted(os.listdir(ORDNER)):
        if datei.endswith(".woff2") and datei not in gewollt:
            os.remove(os.path.join(ORDNER, datei))
            print("  entfernt  %s" % datei)

    gesamt = sum(r[5] for r in regeln)
    print("%s geschrieben — %d Dateien, %.0f KB" %
          (ZIEL_CSS, len(regeln), gesamt / 1024))
    for familie, gewicht, subset, _, _, groesse in regeln:
        print("  %-12s %d  %-9s %5.1f KB" %
              (familie, gewicht, subset, groesse / 1024))


if __name__ == "__main__":
    main()
