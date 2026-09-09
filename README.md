# ckrreinigung.at

Website der **CKR Cleaning Services**, Kufstein — Gebäudereinigung in Tirol.

Statisches HTML, CSS und JavaScript. **Keine Abhängigkeiten, kein
Build-Werkzeug, kein Framework.** Wer diese Seite in fünf Jahren öffnet,
kann sie ändern, ohne vorher irgendetwas zu installieren.

## Was hier wie gebaut wird

Die sechzehn Seiten sind nicht sechzehn handgepflegte Dateien. Kopf, Fuß
und Gerüst stehen an einer Stelle; der Text liegt in `inhalt/`.

| Ordner / Datei | Inhalt |
|---|---|
| `index.html` | Startseite — die einzige von Hand gepflegte Seite |
| `inhalt/leistungen.py` | Text aller zwölf Leistungsseiten |
| `inhalt/seiten.py` | Impressum, Datenschutz, Bewerbung |
| `i18n/tr.json` | Wörterbuch der internen Abnahmefassung |
| `tools/` | Die Skripte, die daraus die Seiten machen |
| `styles.css`, `app.js` | Gestaltung und Verhalten, für alle Seiten |
| `schrift/`, `schriften.css` | Schriften, selbst gehostet |

### Ändern und neu bauen

```sh
sh tools/alles-bauen.sh
```

Baut die Leistungs- und Textseiten, die türkische Abnahmefassung, die
`sitemap.xml` und `robots.txt`.

**Die erzeugten Ordner nicht von Hand bearbeiten** — beim nächsten Lauf
wird darübergeschrieben. Geändert wird in `inhalt/`, in `index.html` oder
in der Vorlage `tools/seiten-bauen.py`.

### Örtlich ansehen

```sh
python3 sunucu.py 8920 .
```

Nicht `python3 -m http.server`: der beherrscht keine HTTP-Bereichsabfragen
(Range), und ohne die lässt sich im Hintergrundvideo nicht springen.

### Schriften erneuern

Nur nötig, wenn eine Schrift oder ein Schnitt dazukommt:

```sh
python3 tools/schriften-holen.py
```

## Entscheidungen, die man kennen sollte

- **Die Adressen sind dieselben wie auf der alten Website.** Der
  Domainname bleibt; wer die Adressen wegwirft, wirft jede
  Google-Platzierung und jeden fremden Link mit weg.
- **Nichts wird von fremden Servern geladen.** Schriften liegen hier,
  YouTube-Videos erst nach einem Klick, das Vorschaubild erst nach
  Zustimmung. Deshalb geht keine IP-Adresse eines Besuchers an Google.
- **Die türkische Fassung unter `/tr/` ist für die interne Abnahme**,
  nicht für Besucher. Sie trägt `noindex` und steht in `robots.txt`.
- **`video-pruefen.html`** ist ein Werkzeug, keine Seite der Website:
  sie sagt in Klartext, was der Browser mit dem Hintergrundvideo macht.

## Noch offen vor dem Umschalten der Domain

1. Impressum: die mit ⚠ markierten Angaben ergänzen, dann `noindex` löschen
2. Datenschutz: Hostinganbieter eintragen, dann `noindex` löschen
3. Einsatzgebiet: die Ortsliste vom Kunden bestätigen lassen
4. `sitemap.xml` in der Google Search Console anmelden

Interne Notizen und Rohmaterial liegen im privaten Depot
`kodozen-kaynak` unter `ckr-material/`.
