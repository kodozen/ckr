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

## Umzug auf ckrreinigung.at

Die Seite läuft zurzeit unter `kodozen.github.io/ckr/` — als Vorschau,
absichtlich für Suchmaschinen gesperrt. Der Grund: `robots.txt` gilt nur
an der Wurzel einer Domain, und die gehört dort dem Konto, nicht diesem
Ordner. Ohne die Sperre käme die Vorschau in den Index und würde später
mit der echten Domain um denselben Text konkurrieren.

**Reihenfolge beim Umschalten:**

1. **Inhaltlich fertig machen**
   - Impressum: die mit ⚠ markierten Angaben ergänzen, dann die Zeile
     `"noindex": True` in `inhalt/seiten.py` entfernen
   - Datenschutz: Hostinganbieter eintragen, ebenso `noindex` entfernen
   - Einsatzgebiet: die Ortsliste vom Kunden bestätigen lassen

2. **DNS beim Registrar setzen** (dort, wo ckrreinigung.at verwaltet wird)

   Für `www.ckrreinigung.at` einen CNAME:

   ```
   www    CNAME    kodozen.github.io.
   ```

   Für die nackte Domain `ckrreinigung.at` vier A-Einträge:

   ```
   @    A    185.199.108.153
   @    A    185.199.109.153
   @    A    185.199.110.153
   @    A    185.199.111.153
   ```

   *Erst danach weitermachen.* Die alte Website ist bis zu diesem Schritt
   unberührt; ab hier zeigt die Domain auf dieses Depot.

3. **Datei `CNAME` anlegen** mit genau einer Zeile:

   ```
   www.ckrreinigung.at
   ```

4. **Zwei Schalter in `.github/workflows/pages.yml` umlegen**

   | Von | Auf | Wirkung |
   |---|---|---|
   | `VORSCHAU: "ja"` | `"nein"` | kein `noindex` mehr, die Seite darf in den Index |
   | `SEITEN_WURZEL=/ckr/` | `SEITEN_WURZEL=/` | die 404-Seite verweist wieder auf die Wurzel |

5. **In den Einstellungen** unter Settings → Pages die Domain eintragen
   und *Enforce HTTPS* einschalten, sobald das Zertifikat ausgestellt ist
   (dauert nach dem DNS-Eintrag meist einige Minuten).

6. **Danach prüfen**
   - `https://www.ckrreinigung.at/sitemap.xml` erreichbar
   - `https://www.ckrreinigung.at/robots.txt` erreichbar — jetzt greift sie
     wirklich, weil die Seite an der Wurzel ihrer eigenen Domain liegt
   - Sitemap in der Google Search Console anmelden
   - Eine Handvoll alter Adressen aufrufen; sie sind absichtlich dieselben
     geblieben und müssen weiter funktionieren

**Nicht vergessen:** die alte WordPress-Installation erst abschalten, wenn
die neue Seite unter der Domain läuft.

Interne Notizen und Rohmaterial liegen im privaten Depot
`kodozen-kaynak` unter `ckr-material/`.
