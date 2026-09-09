# -*- coding: utf-8 -*-
"""Einfache Seiten: Text mit Überschriften, kein eigenes Gerüst.

Kopf und Fuß kommen aus index.html (siehe tools/seiten-bauen.py).
Hier steht nur der Rumpf. Die Adressen sind dieselben wie auf der
alten Website, damit vorhandene Links und Platzierungen halten.
"""

SEITEN = [
{
 "slug": "ihre-bewerbung",
 "titel": "Ihre Bewerbung",
 "beschreibung": "Arbeiten bei CKR Cleaning Services in Kufstein: Lehrstelle Gebäudereinigung, Voll- und Teilzeit, Einstieg auch ohne Vorerfahrung.",
 "noindex": False,
 "rumpf": r'''<h1>Ihre Bewerbung</h1>
    <p class="abschnitt__vorspann">
      Wir bilden aus und suchen laufend. Ein Lebenslauf ist gut, aber
      nicht Bedingung — schreiben Sie uns, wer Sie sind und was Sie suchen.
    </p>

    <h2>Was wir anbieten</h2>
    <ul class="haken">
      <li>Lehrstelle Gebäudereinigung — mit Leuten, die den Beruf seit Jahren machen</li>
      <li>Voll- und Teilzeit, auch geringfügig</li>
      <li>Einstieg ohne Vorerfahrung möglich; eingearbeitet wird bei uns</li>
      <li>Feste Objekte statt täglich wechselnder Einsatzorte, wo es geht</li>
      <li>Ein Team in Kufstein, keine Zentrale in einer anderen Stadt</li>
    </ul>

    <h2>Was wir erwarten</h2>
    <p>
      Pünktlichkeit und Verlässlichkeit — bei einem Schlüssel für ein fremdes
      Haus ist das keine Floskel. Deutsch so weit, dass eine Absprache im Team
      funktioniert. Führerschein ist hilfreich, aber kein Muss.
    </p>

    <h2>So bewerben Sie sich</h2>
    <p>
      Am einfachsten per E-Mail an
      <a href="mailto:info@ckrreinigung.at?subject=Bewerbung">info@ckrreinigung.at</a>.
      Schreiben Sie kurz: Name, wo Sie wohnen, ob Sie Voll- oder Teilzeit
      suchen, und ab wann Sie können. Zeugnisse dürfen Sie mitschicken,
      müssen Sie aber nicht.
    </p>
    <p>
      Lieber telefonisch? <a href="tel:+436508933881">+43 650 893 38 81</a> —
      wir sind rund um die Uhr erreichbar.
    </p>

    <p class="rechtsseite__knoepfe">
      <a class="knopf knopf--voll" href="mailto:info@ckrreinigung.at?subject=Bewerbung">Bewerbung schreiben</a>
      <a class="knopf" href="tel:+436508933881"><span aria-hidden="true">☎</span> Anrufen</a>
    </p>

    <h2>Was mit Ihren Unterlagen passiert</h2>
    <p>
      Ihre Bewerbung verwenden wir ausschließlich für die Besetzung der
      Stelle. Wird nichts daraus, löschen wir die Unterlagen — außer Sie
      sagen ausdrücklich, dass wir sie behalten dürfen.
      Näheres in der <a href="../datenschutzerklaerung/">Datenschutzerklärung</a>.
    </p>''',
},

{
 "slug": "impressum",
 "titel": "Impressum",
 "beschreibung": "Impressum und Offenlegung gemäß § 5 ECG und § 25 MedienG — CKR Cleaning Services, Kufstein.",
 "noindex": True,   # solange unten noch Lücken stehen
 "rumpf": r'''<h1>Impressum</h1>
    <p class="abschnitt__vorspann">
      Offenlegung gemäß § 5 E-Commerce-Gesetz und § 25 Mediengesetz.
    </p>

    <!-- Diese Kästen stehen bewusst auffällig da. Ein Impressum mit
         falschen oder fehlenden Pflichtangaben ist in Österreich
         abmahnfähig — lieber sichtbar unfertig als still falsch. -->
    <p class="luecke" role="note">
      <strong>Noch offen.</strong> Die mit „⚠" markierten Angaben müssen von
      CKR bestätigt werden, bevor diese Seite online geht. Bis dahin ist sie
      für Suchmaschinen gesperrt.
    </p>

    <h2>Medieninhaber und Diensteanbieter</h2>
    <p>
      CKR – Cleaning Services<br>
      Weckaufstraße 10<br>
      6330 Kufstein<br>
      Österreich
    </p>

    <h2>Kontakt</h2>
    <p>
      Telefon: <a href="tel:+436508933881">+43 650 893 38 81</a><br>
      E-Mail: <a href="mailto:info@ckrreinigung.at">info@ckrreinigung.at</a>
    </p>

    <h2>Unternehmensdaten</h2>
    <ul class="rechtsseite__liste">
      <li><span class="luecke__marke">⚠</span> Rechtsform und vollständiger Firmenwortlaut</li>
      <li><span class="luecke__marke">⚠</span> Inhaber / vertretungsbefugte Person</li>
      <li><span class="luecke__marke">⚠</span> Firmenbuchnummer und Firmenbuchgericht (falls eingetragen)</li>
      <li><span class="luecke__marke">⚠</span> UID-Nummer (falls vorhanden)</li>
      <li><span class="luecke__marke">⚠</span> GLN / GISA-Zahl des Gewerbes</li>
    </ul>

    <h2>Gewerbe und Aufsicht</h2>
    <ul class="rechtsseite__liste">
      <li><span class="luecke__marke">⚠</span> Genaue Gewerbebezeichnung laut Gewerbeschein</li>
      <li>Gewerbebehörde: Bezirkshauptmannschaft Kufstein</li>
      <li>Mitglied der Wirtschaftskammer Tirol, Fachgruppe der Denkmal-, Fassaden- und Gebäudereiniger</li>
      <li>Anwendbare Rechtsvorschrift: Gewerbeordnung (GewO), abrufbar unter
        <a href="https://www.ris.bka.gv.at" target="_blank" rel="noopener">ris.bka.gv.at</a></li>
    </ul>

    <h2>Unternehmensgegenstand</h2>
    <p>
      Gebäudereinigung: Unterhalts-, Grund- und Treppenhausreinigung, Glas-,
      Fenster- und Fassadenreinigung, Hotel- und Appartementreinigung, Bau-
      und Endreinigung, Entrümpelung und Hausbetreuung, Teppichreinigung,
      Verkehrsmittelreinigung sowie Denkmalreinigung.
    </p>

    <h2>Online-Streitbeilegung</h2>
    <p>
      Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung
      bereit: <a href="https://ec.europa.eu/consumers/odr" target="_blank" rel="noopener">ec.europa.eu/consumers/odr</a>.
      Wir sind weder verpflichtet noch bereit, an einem Streitbeilegungsverfahren
      vor einer Verbraucherschlichtungsstelle teilzunehmen.
    </p>

    <h2>Haftung für Inhalte und Links</h2>
    <p>
      Die Inhalte dieser Seiten werden mit Sorgfalt erstellt. Für die Richtigkeit,
      Vollständigkeit und Aktualität können wir jedoch keine Gewähr übernehmen.
      Für die Inhalte verlinkter externer Seiten ist ausschließlich deren
      Betreiber verantwortlich.
    </p>

    <h2>Bildnachweis</h2>
    <p>
      Fotos und Videoaufnahmen stammen, soweit nicht anders angegeben, von
      CKR – Cleaning Services.
    </p>''',
},

{
 "slug": "datenschutzerklaerung",
 "titel": "Datenschutzerklärung",
 "beschreibung": "Datenschutzerklärung von CKR Cleaning Services, Kufstein: welche Daten diese Website verarbeitet — und welche nicht.",
 "noindex": True,
 "rumpf": r'''<h1>Datenschutzerklärung</h1>
    <p class="abschnitt__vorspann">
      Diese Website ist bewusst schlank gebaut. Sie setzt keine Cookies, misst
      kein Besucherverhalten und speichert Ihre Anfragen nicht auf einem Server.
      Was trotzdem an Daten anfällt, steht hier.
    </p>

    <p class="luecke" role="note">
      <strong>Noch offen.</strong> Der Hostinganbieter und die
      Verantwortlichen-Angaben müssen ergänzt werden, bevor die Seite online
      geht. Bis dahin ist sie für Suchmaschinen gesperrt.
    </p>

    <h2>Verantwortlicher</h2>
    <p>
      CKR – Cleaning Services, Weckaufstraße 10, 6330 Kufstein, Österreich<br>
      <a href="mailto:info@ckrreinigung.at">info@ckrreinigung.at</a> ·
      <a href="tel:+436508933881">+43 650 893 38 81</a>
    </p>

    <h2>Cookies und Speicherung auf Ihrem Gerät</h2>
    <p>
      Diese Website setzt <strong>keine Cookies</strong>. Gespeichert wird
      genau eine Sache, und nur wenn Sie sie selbst auslösen: Ihre Antwort
      auf die Einwilligungsfrage. Sie liegt im lokalen Speicher Ihres
      Browsers (<em>localStorage</em>, Schlüssel <code>ckr-einwilligung</code>),
      verlässt Ihr Gerät nicht und wird von uns nicht ausgelesen.
    </p>
    <p>
      Bewusst kein Cookie: ein Cookie würde bei jedem Seitenaufruf an den
      Server mitgeschickt. Der lokale Speicher tut das nicht — deshalb
      bleibt der Satz „diese Seite setzt keine Cookies“ auch mit
      Einwilligungsfrage richtig.
    </p>
    <p>
      Sie können Ihre Entscheidung jederzeit ändern: der Link
      <strong>Cookie-Einstellungen</strong> im Seitenfuß öffnet die Frage
      erneut. Löschen Sie die Daten Ihres Browsers für diese Seite, ist die
      Entscheidung ebenfalls weg und wird neu gestellt.
    </p>

    <h2>Was diese Website <em>nicht</em> tut</h2>
    <ul class="rechtsseite__liste">
      <li>Keine Cookies und keine vergleichbaren Speichertechniken.</li>
      <li>Keine Analyse- oder Trackingdienste, kein Google Analytics, kein Pixel.</li>
      <li>Keine Werbenetzwerke, kein Profiling, keine automatisierte Entscheidungsfindung.</li>
      <li>Keine Weitergabe Ihrer Daten zu Werbezwecken.</li>
      <li>Keine Schriften, Karten oder Skripte von fremden Servern.</li>
    </ul>

    <h2>Server-Logdateien</h2>
    <p>
      Beim Abruf der Seiten werden vom Hostinganbieter automatisch technische
      Daten erfasst: IP-Adresse, Zeitpunkt, aufgerufene Datei, übertragene
      Datenmenge, Browsertyp und Betriebssystem. Diese Daten sind für den
      sicheren Betrieb erforderlich, werden nicht mit anderen Quellen
      zusammengeführt und nach kurzer Frist gelöscht.
      Rechtsgrundlage ist das berechtigte Interesse an einem störungsfreien
      Betrieb (Art. 6 Abs. 1 lit. f DSGVO).
    </p>
    <p><span class="luecke__marke">⚠</span> Hostinganbieter und Speicherdauer ergänzen.</p>

    <h2>Anfrageformular</h2>
    <p>
      Das Formular auf der Startseite überträgt <strong>nichts an unseren
      Server</strong>. Es stellt aus Ihren Eingaben eine Nachricht zusammen und
      übergibt sie dem Programm, das Sie selbst wählen: Ihrem E-Mail-Programm
      oder WhatsApp. Erst mit dem Absenden dort verlassen die Daten Ihr Gerät.
    </p>
    <p>
      Wählen Sie WhatsApp, gelten zusätzlich die Datenschutzbestimmungen von
      WhatsApp Ireland Ltd. Wählen Sie E-Mail, erreicht uns die Nachricht über
      Ihren eigenen Mailanbieter.
    </p>
    <p>
      Ihre Angaben verwenden wir ausschließlich, um Ihre Anfrage zu beantworten
      (Art. 6 Abs. 1 lit. b DSGVO). Wir bewahren sie so lange auf, wie es für
      die Bearbeitung und die gesetzlichen Aufbewahrungspflichten nötig ist.
    </p>

    <h2>Schriftarten</h2>
    <p>
      Die verwendeten Schriften „Archivo“ und „Public Sans“ liegen auf unserem
      eigenen Server und werden von dort geladen. Es besteht <strong>keine
      Verbindung zu Google Fonts</strong> oder einem anderen fremden Anbieter;
      Ihre IP-Adresse wird dabei an niemanden übertragen.
    </p>

    <h2>YouTube-Videos</h2>
    <p>
      Videos werden nicht automatisch geladen. Ohne Ihre Zustimmung zu
      <em>externen Medien</em> sehen Sie eine Karte, die vollständig von
      unserem eigenen Server kommt — <strong>auch das Vorschaubild</strong>
      wird dann nicht bei Google geholt. Erst Ihr Klick lädt das Video von
      YouTube (Google Ireland Ltd.), und zwar über die erweiterte
      Datenschutzeinstellung („youtube-nocookie&#34;). Bis dahin besteht
      keinerlei Verbindung zu Google.
    </p>

    <h2>Verlinkte soziale Netzwerke</h2>
    <p>
      Die Verweise auf Instagram und Facebook sind einfache Links. Es sind keine
      Schaltflächen der Netzwerke eingebunden; eine Verbindung entsteht erst,
      wenn Sie den Link anklicken.
    </p>

    <h2>Ihre Rechte</h2>
    <p>
      Sie haben das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung
      der Verarbeitung, Datenübertragbarkeit und Widerspruch. Wenden Sie sich
      dafür an <a href="mailto:info@ckrreinigung.at">info@ckrreinigung.at</a>.
    </p>
    <p>
      Sie können sich außerdem bei der Aufsichtsbehörde beschweren:
      Österreichische Datenschutzbehörde, Barichgasse 40–42, 1030 Wien,
      <a href="https://www.dsb.gv.at" target="_blank" rel="noopener">dsb.gv.at</a>.
    </p>''',
},
]

NACH_SLUG = {s["slug"]: s for s in SEITEN}
