# -*- coding: utf-8 -*-
"""Inhalt aller Leistungsseiten — eine Datei, dreizehn Seiten.

Warum so: dreizehn handgeschriebene HTML-Dateien driften auseinander.
Ändert sich die Telefonnummer, der Kopf oder ein Gestaltungsdetail,
muss man dreizehn Stellen finden. Hier steht der Text, das Gerüst
steht in tools/seiten-bauen.py — und jede Seite entsteht neu, wenn
sich eines von beidem ändert.

Die Adressen (slug) sind bewusst dieselben wie auf der alten Website.
Der Domainname bleibt; wer die alten Adressen wegwirft, wirft jede
Google-Platzierung und jeden fremden Link mit weg.

Felder
------
slug        Adresse, ohne Schrägstriche
titel       <title> und H1
marker      Kleine Zeile über der Überschrift
vorspann    Ein Satz, der die Seite trägt
kern        Absätze mit dem eigentlichen Argument
punkte      Was dazugehört — die Prüfliste
warum       (Überschrift, Text) — warum es sich lohnt
fragen      Seiteneigene Fragen und Antworten
verwandt    Slugs verwandter Leistungen
gruppe      Für die Übersicht auf der Startseite
"""

LEISTUNGEN = [

{
 "slug": "unterhaltsreinigung",
 "bild_alt": 'Bürogang nach der täglichen Reinigung, Reinigungswagen mit Mopp und Eimer an der Wand, Boden feucht gewischt.',
 "gruppe": "Gebäude & Unterhalt",
 "titel": "Unterhaltsreinigung",
 "marker": "Laufende Reinigung",
 "kurz": "Die Reinigung, die niemandem auffällt — solange sie stimmt.",
 "vorspann": "Büros, Praxen, öffentliche Bereiche: Sauberkeit, die jeden Tag "
             "gleich aussieht, ohne dass Sie daran denken müssen.",
 "kern": [
   "Unterhaltsreinigung ist die Arbeit, über die niemand spricht, solange sie "
   "gemacht wird. Fällt sie zwei Wochen aus, spricht plötzlich jeder darüber. "
   "Genau deshalb ist sie unser Schwerpunkt: nicht der einmalige große "
   "Einsatz, sondern der gleichbleibende Zustand.",
   "Wir arbeiten mit ökologischen Produkten und mit Maschinen, die zum "
   "jeweiligen Verfahren passen — nicht mit dem, was gerade im Wagen liegt. "
   "Unser Personal wird von geschulten Objektleitern eingewiesen, betreut und "
   "regelmäßig kontrolliert. Wenn etwas nicht passt, merken wir es, bevor Sie "
   "es melden müssen.",
 ],
 "punkte": [
   "Büroräume, Besprechungs- und Sozialräume",
   "Sanitäranlagen und Teeküchen",
   "Verkehrsflächen, Eingänge und Aufzüge",
   "Öffentlich zugängliche Bereiche",
   "Abfallentsorgung und Verbrauchsmaterial",
   "Reinigungsplan nach Ihren Betriebszeiten",
 ],
 "warum": ("Warum ein fester Plan mehr bringt als ein günstiger Stundensatz",
   "Ein Reinigungsplan hält fest, was wann gemacht wird — täglich, wöchentlich, "
   "monatlich. Das klingt bürokratisch und ist der einzige Grund, warum eine "
   "Unterhaltsreinigung über Jahre gleich gut bleibt. Ohne Plan wird immer das "
   "gereinigt, was gerade auffällt, und der Rest verschwindet langsam."),
 "fragen": [
   ("Arbeiten Sie außerhalb unserer Betriebszeiten?",
    "Ja, das ist sogar der Normalfall. Früh morgens, abends oder am Wochenende "
    "— wie es Ihren Ablauf am wenigsten stört."),
   ("Bekommen wir immer dasselbe Personal?",
    "So weit es geht, ja. Wer ein Objekt kennt, arbeitet schneller und "
    "übersieht weniger. Bei Urlaub und Krankheit springt eingewiesenes "
    "Personal ein, kein Fremder."),
 ],
 "verwandt": ["treppenhausreinigung", "grundreinigung", "glasreinigung"],
},

{
 "slug": "treppenhausreinigung",
 "bild_alt": 'Gereinigtes Stiegenhaus mit gefliesten Stufen und weißem Geländer, Blick die Treppe hinauf.',
 "gruppe": "Gebäude & Unterhalt",
 "titel": "Treppenhausreinigung",
 "marker": "Wohn- und Bürohäuser",
 "kurz": "Damit Sie nicht alles selber machen müssen.",
 "vorspann": "Stiegenhäuser sind der erste Eindruck eines Hauses — und die "
             "Fläche, über die sich Hausgemeinschaften am häufigsten streiten.",
 "kern": [
   "Unsere Mitarbeiter wissen, worauf es im Stiegenhaus ankommt: die Kanten "
   "der Stufen, die Handläufe, die Ecken hinter den Türen, der Bereich vor den "
   "Briefkästen. Deshalb erreichen wir ein gutes Ergebnis in kurzer Zeit — "
   "und kurze Zeit ist bei einer Fläche, die jede Woche drankommt, der ganze "
   "Unterschied im Preis.",
   "Eine regelmäßige Stiegenhausreinigung nimmt außerdem eine Aufgabe aus der "
   "Hausgemeinschaft heraus, die dort erfahrungsgemäß niemand freiwillig "
   "übernimmt.",
 ],
 "punkte": [
   "Stufen, Podeste und Handläufe",
   "Eingangsbereich und Windfang",
   "Aufzugkabine und Türen",
   "Fenster im Stiegenhaus",
   "Kellerabgänge und Nebenräume",
   "Müllraum auf Wunsch",
 ],
 "warum": ("Nicht nur optisch",
   "Regelmäßige Reinigung hält Abnutzung an Treppen, Handläufen und Türen "
   "gering — Streusalz, Sand und Feuchtigkeit greifen Beläge an, wenn sie "
   "liegen bleiben. Nebenbei fallen Schwachstellen früh auf: eine lose Stufe, "
   "ein tropfender Hahn, ein defektes Licht. Wir sagen Ihnen Bescheid."),
 "fragen": [
   ("In welchem Rhythmus wird gereinigt?",
    "Üblich sind einmal oder zweimal pro Woche, je nach Anzahl der Parteien "
    "und Lage. Im Winter oft häufiger, weil Streusplitt hereingetragen wird."),
   ("Übernehmen Sie auch den Winterdienst?",
    "Das klären wir im Einzelfall bei der Besichtigung — sprechen Sie uns "
    "darauf an."),
 ],
 "verwandt": ["unterhaltsreinigung", "grundreinigung", "entruempelung-hausbetreuung"],
},

{
 "slug": "grundreinigung",
 "bild_alt": 'Scheuersaugmaschine auf einer großen Hallenfläche; hinter ihr ist der Boden sichtbar heller als davor.',
 "gruppe": "Gebäude & Unterhalt",
 "titel": "Grundreinigung",
 "marker": "Einmal richtig tief",
 "kurz": "Weil „nur“ sauber manchmal nicht genügt.",
 "vorspann": "Die Ecken und Nischen, die Sie seit Jahren nicht mehr gesehen "
             "haben — und die Beläge, die unter der laufenden Reinigung "
             "trotzdem stumpf geworden sind.",
 "kern": [
   "Eine Grundreinigung ist keine gründlichere Unterhaltsreinigung, sie ist "
   "etwas anderes: Beschichtungen werden abgetragen und neu aufgebaut, "
   "Fugen aufgearbeitet, Ablagerungen entfernt, die sich über Jahre "
   "festgesetzt haben. Danach greift die laufende Reinigung wieder.",
   "Unsere Spezialisten erstellen dafür einen Plan, der auf Ihr Objekt "
   "zugeschnitten ist. Weil unser Team dabei mit Ihren persönlichen "
   "Gegenständen in Berührung kommt, zählen bei der Personalauswahl "
   "Verantwortungsbewusstsein, Diskretion und Zuverlässigkeit.",
 ],
 "punkte": [
   "Böden entschichten und neu einpflegen",
   "Fugen und Silikonanschlüsse",
   "Heizkörper, Rohre und Sockelleisten",
   "Türen, Zargen und Lichtschalter",
   "Küchen- und Sanitärbereiche komplett",
   "Fenster innen samt Rahmen und Falz",
 ],
 "warum": ("Der richtige Zeitpunkt",
   "Vor dem Einzug, nach einem Auszug, vor einer Übergabe — oder einmal im "
   "Jahr als fester Termin. Wer regelmäßig grundreinigen lässt, braucht "
   "seltener neue Beläge. Das ist der Punkt, an dem sich die Ausgabe rechnet."),
 "fragen": [
   ("Wie lange dauert eine Grundreinigung?",
    "Das hängt von Fläche und Zustand ab. Nach der Besichtigung nennen wir "
    "Ihnen Dauer und Fixpreis — beides verbindlich."),
   ("Müssen wir ausräumen?",
    "Nur was empfindlich ist. Möbel rücken wir selbst; sagen Sie uns, was "
    "besser stehen bleibt."),
 ],
 "verwandt": ["unterhaltsreinigung", "teppichreinigung", "baureinigung-endreinigung"],
},

{
 "slug": "glasreinigung",
 "bild_alt": 'Schaufensterfront einer Ladenzeile, streifenfrei gereinigt; davor stehen Abzieher und Eimer auf dem Gehsteig.',
 "gruppe": "Glas, Fassade & Dach",
 "titel": "Glasreinigung",
 "marker": "Innen und außen",
 "kurz": "Das Erste, was ein Besucher von Ihrem Haus sieht.",
 "vorspann": "Schaufenster, Eingangstüren, Wintergärten, Glastrennwände — "
             "streifenfrei, auch dort, wo man eine Leiter braucht.",
 "kern": [
   "Glas verzeiht nichts. Ein Streifen, den man bei Sonnenlicht sieht, ist "
   "auffälliger als ein ganzer Raum, der nur mittelmäßig gereinigt wurde. "
   "Deshalb arbeiten wir mit Abzieher und entmineralisiertem Wasser statt mit "
   "Tuch und Reiniger — die Fläche trocknet ohne Rückstand.",
   "Rahmen, Falz und Dichtungen gehören dazu. Wird nur die Scheibe gemacht, "
   "läuft beim nächsten Regen der Schmutz aus dem Rahmen wieder über das Glas.",
 ],
 "punkte": [
   "Schaufenster und Eingangsverglasung",
   "Fenster innen und außen",
   "Rahmen, Falz und Dichtungen",
   "Glastrennwände und Geländer",
   "Wintergärten und Überkopfverglasung",
   "Regelmäßig oder einmalig",
 ],
 "warum": ("Warum entmineralisiertes Wasser",
   "Normales Leitungswasser hinterlässt beim Trocknen Kalk — das sind die "
   "Flecken, die man erst sieht, wenn die Sonne darauf steht. Mit entsalztem "
   "Wasser trocknet die Scheibe rückstandsfrei, ganz ohne Nachpolieren. "
   "Das geht auch in Höhen, in denen niemand mehr mit dem Tuch hinkommt."),
 "fragen": [
   ("Wie oft sollte gereinigt werden?",
    "Schaufenster in Fußgängerlage meist wöchentlich bis monatlich, Bürofenster "
    "zwei- bis viermal im Jahr. An stark befahrenen Straßen häufiger."),
   ("Reinigen Sie auch in größerer Höhe?",
    "Ja, bis zu der Höhe, die mit Teleskopstange sicher erreichbar ist. Alles "
    "darüber sehen wir uns bei der Besichtigung an."),
 ],
 "verwandt": ["fenster-und-fassadenreinigung", "unterhaltsreinigung", "hotelreinigung"],
},

{
 "slug": "fenster-und-fassadenreinigung",
 "bild_alt": 'Hausfassade, deren linke Hälfte frisch gewaschen und deutlich heller ist als die rechte; Leiter und Schlauch stehen bereit.',
 "gruppe": "Glas, Fassade & Dach",
 "titel": "Fenster- & Fassadenreinigung",
 "marker": "Was von außen gesehen wird",
 "kurz": "Ein Haus wird von außen beurteilt, bevor jemand hineingeht.",
 "vorspann": "Fassaden, Fenster, Vordächer und Balkone — mit dem Verfahren, "
             "das der Oberfläche entspricht, nicht mit dem stärksten.",
 "kern": [
   "Fassadenreinigung ist vor allem eine Frage des richtigen Drucks. Putz, "
   "Klinker, Holz, Glas und beschichtetes Blech vertragen sehr "
   "Unterschiedliches. Wer überall gleich stark arbeitet, spart eine halbe "
   "Stunde und beschädigt die Oberfläche.",
   "Wir sehen uns die Fassade deshalb vorher an, prüfen an einer unauffälligen "
   "Stelle und legen erst dann das Verfahren fest. Bei Algen- und Moosbefall "
   "gehört eine Nachbehandlung dazu, sonst ist der Belag in zwei Jahren zurück.",
 ],
 "punkte": [
   "Putz-, Klinker- und Holzfassaden",
   "Fenster außen samt Rahmen",
   "Balkone, Geländer und Vordächer",
   "Algen-, Moos- und Grünbelagentfernung",
   "Graffitientfernung nach Absprache",
   "Dach- und Solaranlagenreinigung",
 ],
 "warum": ("Sauber ist nicht nur schöner",
   "Grünbelag und Verschmutzung halten Feuchtigkeit in der Fassade. Feuchte "
   "Fassaden dämmen schlechter und frieren im Winter auf. Eine Reinigung alle "
   "paar Jahre ist deutlich günstiger als der Anstrich, den man sich damit "
   "erspart."),
 "fragen": [
   ("Welche Jahreszeit ist die richtige?",
    "Frühjahr bis Herbst. Bei Frost lässt sich weder reinigen noch "
    "nachbehandeln."),
   ("Brauchen Sie ein Gerüst?",
    "Meistens nicht. Was ohne Gerüst erreichbar ist, klären wir bei der "
    "kostenlosen Besichtigung."),
 ],
 "verwandt": ["glasreinigung", "baureinigung-endreinigung", "denkmalreinigung"],
},

{
 "slug": "hotelreinigung",
 "bild_alt": 'Hergerichtetes Hotelzimmer mit frisch bezogenem Bett und gefalteten Handtüchern.',
 "gruppe": "Objekt & Gewerbe",
 "titel": "Hotelreinigung",
 "marker": "Für Hotels und Pensionen",
 "kurz": "Zimmer, die bis zum Check-in fertig sein müssen.",
 "vorspann": "In Tirol entscheidet die Sauberkeit des Zimmers über die "
             "Bewertung — und die Bewertung über die nächste Buchung.",
 "kern": [
   "Hotelreinigung ist Arbeit gegen die Uhr. Zwischen Check-out und Check-in "
   "liegen wenige Stunden, und in dieser Zeit muss jedes Zimmer denselben "
   "Zustand erreichen. Das schafft man nicht mit Tempo allein, sondern mit "
   "einer festen Reihenfolge, die jeder im Team kennt.",
   "Wir richten uns nach Ihrer Belegung, nicht umgekehrt. In der Hochsaison "
   "mehr Personal, in der Zwischensaison die Arbeiten, für die sonst keine "
   "Zeit ist: Grundreinigung der Zimmer, Teppiche, Fenster, Wellnessbereich.",
 ],
 "punkte": [
   "Zimmerreinigung und Abreisereinigung",
   "Bäder und Sanitärbereiche",
   "Frühstücksraum und Restaurant",
   "Lobby, Gänge und Stiegenhaus",
   "Wellness-, Sauna- und Fitnessbereich",
   "Grundreinigung in der Zwischensaison",
 ],
 "warum": ("Was Gäste tatsächlich bemerken",
   "In Bewertungen tauchen immer dieselben Punkte auf: Haare im Bad, Staub "
   "auf Ablagen, Flecken auf dem Teppich, Fenster mit Rand. Das sind fünf "
   "Stellen — und genau die stehen bei uns auf der Prüfliste des "
   "Objektleiters, der die Zimmer stichprobenartig nachkontrolliert."),
 "fragen": [
   ("Können Sie kurzfristig aufstocken?",
    "Ja. Wir sind rund um die Uhr erreichbar; bei unerwarteter Auslastung "
    "oder Ausfällen im eigenen Team melden Sie sich einfach."),
   ("Übernehmen Sie auch Ferienwohnungen?",
    "Ja, dafür gibt es eigene Rhythmen — siehe Appartementreinigung."),
 ],
 "verwandt": ["appartementreinigung", "teppichreinigung", "glasreinigung"],
},

{
 "slug": "appartementreinigung",
 "bild_alt": 'Ferienwohnung bezugsfertig: bezogenes Bett, gestapelte Handtücher, abgewischte Küchenzeile, Schlüssel auf der Ablage.',
 "gruppe": "Objekt & Gewerbe",
 "titel": "Appartementreinigung",
 "marker": "Wohnung, Haus & Ferienappartement",
 "kurz": "Ihr Zuhause in vertrauenswürdigen Händen.",
 "vorspann": "Häufigkeit, Umfang und Intensität legen wir gemeinsam fest — "
             "das Team arbeitet zeitlich flexibel, damit es in Ihren "
             "Wochenplan passt.",
 "kern": [
   "Bei einer Privatwohnung geht es um mehr als um das Ergebnis. Es geht "
   "darum, wer hereinkommt, wann, und ob Sie dabei sein müssen. Deshalb "
   "arbeiten wir mit festem Personal und stimmen die Zeiten so ab, dass Sie "
   "nicht gestört werden.",
   "Der Umfang steht unten, aber er ist keine feste Liste zum Abhaken: was "
   "Sie nicht brauchen, lassen wir weg, was fehlt, nehmen wir dazu.",
 ],
 "punkte": [
   "Böden: Laminat, PVC, Fayence- und Keramikfliesen",
   "Böden Spezial: Parkett, Beton, Steinfliesen",
   "Ablageflächen und Möbeloberflächen",
   "Bad: Oberflächen, Sanitär, Wanne, Dusche, WC",
   "Küche: Oberflächen, Backofen, Herd, komplett",
   "Balkon und auf Wunsch Haushaltsgeräte",
 ],
 "warum": ("Drei Rhythmen",
   "Wöchentlich für bewohnte Wohnungen und Häuser. Vierzehntägig — der "
   "häufigste Fall — für die meisten Haushalte und ruhiger belegte "
   "Ferienwohnungen. Einmalig nach Auszug, vor Übergabe oder nach einem Umbau. "
   "Welcher passt, sehen wir bei der Besichtigung."),
 "fragen": [
   ("Müssen wir zu Hause sein?",
    "Nein. Viele Kundinnen und Kunden hinterlegen einen Schlüssel. Wir gehen "
    "damit so um, wie man mit einem fremden Schlüssel umgehen muss."),
   ("Bringen Sie die Mittel mit?",
    "Ja, alles. Wenn Sie bestimmte Produkte verwendet haben möchten — etwa "
    "wegen einer Allergie oder einer empfindlichen Oberfläche — sagen Sie es "
    "uns einfach."),
 ],
 "verwandt": ["hotelreinigung", "grundreinigung", "teppichreinigung"],
},

{
 "slug": "teppichreinigung",
 "bild_alt": 'Sprühextraktion auf grauem Teppichboden; die gereinigte Bahn hebt sich hell vom übrigen Boden ab.',
 "gruppe": "Objekt & Gewerbe",
 "titel": "Teppichreinigung",
 "marker": "Teppiche und Polster",
 "kurz": "Was im Teppich steckt, sieht man nicht — man atmet es.",
 "vorspann": "Abgewohnte Teppiche machen keinen schlechten Eindruck. Sie "
             "sammeln Keime und Bakterien und werden zum Gesundheitsrisiko.",
 "kern": [
   "Es gibt drei Gründe, einen Teppich reinigen zu lassen, und der optische "
   "ist der schwächste. Der zweite sind Keime, Bakterien und Schimmelsporen, "
   "die sich in den Fasern halten. Der dritte ist Geld: je mehr Staub und "
   "Sand sich einlagert, desto schneller zerstören die scharfkantigen "
   "Teilchen Oberflächenstruktur und Farbe.",
   "Eine regelmäßige Reinigung verlängert die Lebensdauer Ihrer Bodenbeläge "
   "deutlich — die Rechnung geht bei jedem Teppich auf, der mehr gekostet hat "
   "als die Reinigung.",
 ],
 "punkte": [
   "Teppichböden in Büro, Hotel und Wohnung",
   "Lose Teppiche und Läufer",
   "Polstermöbel und Sessel",
   "Fleckentfernung und Geruchsbehandlung",
   "Sprüh-Extraktion und Trockenverfahren",
   "Nach Absprache über Nacht",
 ],
 "warum": ("Warum das Verfahren zählt",
   "Zu viel Wasser im falschen Belag heißt lange Trockenzeit und im "
   "schlimmsten Fall Schimmel im Unterboden. Wir wählen das Verfahren nach "
   "Fasern und Rücken des Teppichs — und sagen Ihnen vorher, wann die Fläche "
   "wieder benutzbar ist."),
 "fragen": [
   ("Wie lange dauert das Trocknen?",
    "Je nach Verfahren zwischen zwei und zwölf Stunden. In Büros und Hotels "
    "arbeiten wir deshalb meist abends."),
   ("Gehen alle Flecken raus?",
    "Nicht alle — Rotwein, Tinte und Farbe sind ehrlich gesagt Glückssache, "
    "besonders wenn sie eingetrocknet sind. Wir sagen Ihnen vorher, was wir "
    "realistisch erwarten."),
 ],
 "verwandt": ["grundreinigung", "hotelreinigung", "appartementreinigung"],
},

{
 "slug": "baureinigung-endreinigung",
 "bild_alt": 'Fertiggestellter, leerer Raum vor der Übergabe; der Estrich ist besenrein, die Fensterrahmen sind von Mörtelresten befreit.',
 "gruppe": "Bau & Räumung",
 "titel": "Baureinigung & Endreinigung",
 "marker": "Neubau, Umbau, Sanierung",
 "kurz": "Wenn die Handwerker weg sind und übergeben werden soll.",
 "vorspann": "Wo gespachtelt, gebohrt und gemauert wird, entsteht grober "
             "Schmutz — und die frische Bausubstanz verträgt keine harte Hand.",
 "kern": [
   "Bei Neu- und Umbauten kommt schweres Gerät zum Einsatz. Der Schmutz, den "
   "das hinterlässt, muss gründlich und zugleich schonend weg: frischer Putz, "
   "neue Beschichtungen und montierte Beschläge nehmen sonst Schaden, bevor "
   "das Gebäude überhaupt genutzt wurde.",
   "Genauso wichtig ist der Zeitpunkt. Unsere Fachkräfte fügen sich in den "
   "Bauablauf ein, ohne die eng getakteten Termine der anderen Gewerke zu "
   "stören — Baugrobreinigung während der Bauphase, Bauendreinigung vor der "
   "Übergabe.",
 ],
 "punkte": [
   "Baugrobreinigung während der Bauphase",
   "Bauendreinigung vor der Übergabe",
   "Entfernen von Mörtel-, Farb- und Kleberesten",
   "Fenster, Rahmen und Beschläge",
   "Sanitär, Fliesen und Fugen",
   "Bauschutt und Verpackungsmaterial",
 ],
 "warum": ("Zwei Reinigungen, nicht eine",
   "Wird nur am Ende gereinigt, ist der Bauschmutz längst in Fugen, Falzen "
   "und Silikon eingetrocknet — das kostet mehr Zeit, als die "
   "Zwischenreinigung gekostet hätte. Deshalb planen wir sie mit ein, wenn "
   "der Bauablauf es zulässt."),
 "fragen": [
   ("Wie kurzfristig können Sie kommen?",
    "Bauabnahmen verschieben sich, das kennen wir. Rufen Sie an, sobald der "
    "Termin steht — und noch einmal, wenn er sich ändert."),
   ("Entsorgen Sie auch?",
    "Verpackungsmaterial und Bauschutt in haushaltsüblichem Umfang ja. "
    "Größere Mengen klären wir bei der Besichtigung."),
 ],
 "verwandt": ["entruempelung-hausbetreuung", "grundreinigung", "fenster-und-fassadenreinigung"],
},

{
 "slug": "entruempelung-hausbetreuung",
 "bild_alt": 'Geräumter Kellerraum nach der Entrümpelung: leerer, gefegter Boden, Besen an der Wand, gestapelte Kartons an der Tür.',
 "gruppe": "Bau & Räumung",
 "titel": "Entrümpelung & Hausbetreuung",
 "marker": "Räumung und Übergabe",
 "kurz": "Kostenlose Besichtigung, Fixpreis, besenreine Übergabe.",
 "vorspann": "Entrümpelungen, Haushaltsauflösungen, Wohnungs- und "
             "Verlassenschaftsräumungen — oft in Situationen, in denen "
             "niemand Lust auf Überraschungen hat.",
 "kern": [
   "Vor jeder Entrümpelung bieten wir einen kostenfreien Besichtigungstermin "
   "und einen unverbindlichen Kostenvoranschlag. Bei diesem Termin klären wir "
   "alle Details zu Kosten und Ablauf und nennen sofort den Preis — Fix- oder "
   "Pauschalpreis, beziehungsweise den möglichen Wertausgleich.",
   "Nach der Entrümpelung übergeben wir das Objekt selbstverständlich "
   "besenrein: leer und gekehrt. Soll darüber hinaus gereinigt werden, sagen "
   "Sie es einfach dazu.",
 ],
 "punkte": [
   "Entrümpelung von Wohnung, Haus, Keller und Dachboden",
   "Haushaltsauflösung",
   "Verlassenschaftsräumung",
   "Fachgerechte Entsorgung und Trennung",
   "Wertausgleich bei verwertbarem Inventar",
   "Besenreine Übergabe",
 ],
 "warum": ("Warum wir vorher kommen",
   "Am Telefon lässt sich eine Räumung nicht schätzen. Entscheidend sind "
   "Menge, Stockwerk, Zugang, Aufzug und was entsorgt werden muss — das sieht "
   "man in zwanzig Minuten vor Ort und sonst nirgends. Danach steht der Preis "
   "und ändert sich nicht mehr."),
 "fragen": [
   ("Was passiert mit brauchbaren Sachen?",
    "Was sich verwerten lässt, rechnen wir als Wertausgleich gegen. Was "
    "gespendet werden soll, geben Sie uns mit."),
   ("Wie schnell kann geräumt werden?",
    "Nach der Besichtigung meist innerhalb weniger Tage. Bei Übergabefristen "
    "sagen Sie uns den Termin, wir richten uns danach."),
 ],
 "verwandt": ["baureinigung-endreinigung", "grundreinigung", "treppenhausreinigung"],
},

{
 "slug": "verkehrsmittelreinigung",
 "bild_alt": 'Leerer Nahverkehrswagen bei Nacht nach der Reinigung, Sitze und Haltestangen sauber.',
 "gruppe": "Besondere Aufträge",
 "titel": "Verkehrsmittelreinigung",
 "marker": "Züge, Busse und Straßenbahnen",
 "kurz": "Service im Minutentakt.",
 "vorspann": "Ein Fahrzeug, das gereinigt wird, fährt nicht. Deshalb zählt "
             "hier jede Minute — und ein festes Team, das den Ablauf kennt.",
 "kern": [
   "Verkehrsmittelreinigung ist die ungewöhnlichste Arbeit, die wir machen, "
   "und die mit dem engsten Zeitfenster. Zwischen zwei Umläufen bleiben oft "
   "wenige Minuten; in der Nacht steht das gesamte Depot zur Verfügung. "
   "Beides erfordert eine andere Planung als ein Bürogebäude.",
   "Wir arbeiten nach Ihrem Fahrplan, nicht nach unserem. Unterhaltsreinigung "
   "im Umlauf, Grundreinigung in der Nacht oder an Standtagen — abgestimmt "
   "auf den Dienstplan.",
 ],
 "punkte": [
   "Innenreinigung im Umlauf",
   "Grundreinigung in der Nacht",
   "Sitze, Polster und Haltestangen",
   "Böden und Einstiegsbereiche",
   "Scheiben innen und außen",
   "Sonderreinigung nach Vorfällen",
 ],
 "warum": ("Warum ein festes Team",
   "Wer ein Fahrzeug zum ersten Mal reinigt, sucht: den Wasseranschluss, den "
   "Schalter, die Abfallklappe. Dieses Suchen kostet genau die Minuten, die "
   "nicht da sind. Ein eingespieltes Team fängt sofort an — das ist der ganze "
   "Unterschied zwischen zwölf und zwanzig Minuten pro Wagen."),
 "fragen": [
   ("Arbeiten Sie nachts?",
    "Ja. Bei Verkehrsmitteln ist die Nacht eher die Regel als die Ausnahme."),
   ("Auch nach besonderen Vorfällen?",
    "Ja. Rufen Sie an, wir sind rund um die Uhr erreichbar."),
 ],
 "verwandt": ["unterhaltsreinigung", "teppichreinigung", "glasreinigung"],
},

{
 "slug": "denkmalreinigung",
 "bild_alt": 'Historische Sandsteinfassade mit einer gereinigten Probefläche, die deutlich heller ist als der nachgedunkelte Stein daneben.',
 "gruppe": "Besondere Aufträge",
 "titel": "Denkmalreinigung",
 "marker": "Historische Substanz",
 "kurz": "Alte Fassaden vertragen keine Routine.",
 "vorspann": "Naturstein, historischer Putz und alte Ziegel reagieren "
             "unterschiedlich — hier entscheidet das Verfahren, nicht die "
             "Leistung des Geräts.",
 "kern": [
   "An denkmalgeschützter Substanz ist der stärkste Reiniger immer der "
   "falsche. Was einmal abgetragen ist, kommt nicht zurück. Deshalb wird jede "
   "Fläche vorher geprüft und das Verfahren an einer unauffälligen Stelle "
   "getestet, bevor irgendetwas großflächig passiert.",
   "Wo Auflagen der Denkmalbehörde bestehen, richten wir uns danach und "
   "stimmen uns mit den Verantwortlichen ab. Das dauert länger. Bei einem "
   "Gebäude, das seit dreihundert Jahren steht, ist das die richtige "
   "Reihenfolge.",
 ],
 "punkte": [
   "Naturstein und historischer Putz",
   "Sichtziegel und Sichtbeton",
   "Schonende Verfahren mit geringem Druck",
   "Probefläche vor der Ausführung",
   "Grünbelag- und Krustenentfernung",
   "Abstimmung mit den Auflagen",
 ],
 "warum": ("Erst die Probe, dann die Fläche",
   "Eine Probefläche kostet eine halbe Stunde und beantwortet die einzige "
   "Frage, die zählt: Was verträgt dieser Stein? Ohne sie arbeitet man mit "
   "einer Vermutung an etwas, das sich nicht ersetzen lässt."),
 "fragen": [
   ("Arbeiten Sie mit der Denkmalbehörde zusammen?",
    "Wo Auflagen bestehen, richten wir uns danach und stimmen das Verfahren "
    "vorher ab."),
   ("Machen Sie auch kleine Flächen?",
    "Ja — ein Portal, eine Treppe, eine Fassadenseite. Sprechen Sie uns an."),
 ],
 "verwandt": ["fenster-und-fassadenreinigung", "glasreinigung", "grundreinigung"],
},

]

# Nach Slug greifbar machen
NACH_SLUG = {l["slug"]: l for l in LEISTUNGEN}
