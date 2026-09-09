#!/bin/sh
# Baut alles Erzeugte neu. Ein Befehl, damit nie eine Datei zurückbleibt.
#
#   sh tools/alles-bauen.sh
#
# Die Schriften fehlen hier bewusst: die holt man einmal
# (python3 tools/schriften-holen.py) und danach nie wieder.
set -e
cd "$(dirname "$0")/.."
echo "— Leistungs- und Textseiten"
python3 tools/seiten-bauen.py
echo
echo "— Türkische Abnahmefassung"
python3 tools/uebersetzen.py tr
echo
echo "— Sitemap und robots.txt"
python3 tools/sitemap-bauen.py
