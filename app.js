/* CKR Cleaning Services — keine Abhängigkeiten, kein Build-Schritt.

   Alles, was der Kunde später ändern will, steht oben in den Listen:
   Leistungen, Sprachen, Videos. Wer eine Leistung streicht oder eine
   Video-ID einträgt, muss nichts anderes anfassen. */
(function () {
  "use strict";

  document.documentElement.classList.add("js");

  /* ==========================================================
     Einstellungen
     ========================================================== */

  var TELEFON_WA = "436508933881";              // WhatsApp, ohne + und Leerzeichen
  var EMAIL = "info@ckrreinigung.at";

  /* Das Formular steht nur auf der Startseite. Von einer Unterseite
     aus muss der Weg dorthin eine Ebene hoch gehen. */
  var ZUM_ANGEBOT = document.querySelector("[data-formular]") ? "#angebot" : "../#angebot";
  var ZUM_DATENSCHUTZ = document.querySelector("[data-formular]")
    ? "datenschutzerklaerung/" : "../datenschutzerklaerung/";

  /* Reihenfolge = Reihenfolge im Formular. Der Kunde weiß noch nicht,
     womit er am meisten verdient; sobald er es sagt, wird hier
     umsortiert und sonst nirgends. */
  var LEISTUNGEN = [
    "Unterhaltsreinigung",
    "Treppenhausreinigung",
    "Grundreinigung",
    "Allgemeine Raumpflege",
    "Büro- und Privatreinigung",
    "Glasreinigung",
    "Fenster- & Fassadenreinigung",
    "Dachreinigung",
    "Solaranlagenreinigung",
    "Hotelreinigung",
    "Appartementreinigung",
    "Werkstattreinigung",
    "Baureinigung & Endreinigung",
    "Entrümpelung & Hausbetreuung",
    "Teppichreinigung",
    "Verkehrsmittelreinigung",
    "Denkmalreinigung"
  ];

  /* Sprachen. Deutsch ist die Quelle, die anderen entstehen daraus.

     Türkisch ist bewusst `intern: true`: die Fassung dient allein der
     Abnahme durch die Agentur und steht nicht im Umschalter. Auf der
     Website eines Kufsteiner Reinigungsbetriebs hätte eine türkische
     Sprachwahl für Kunden keinen Nutzen und würde die Suchmaschinen
     auf eine Sprache lenken, die im Zielmarkt niemand sucht. Die
     Seite bleibt über /tr/ erreichbar, trägt dort aber noindex. */
  var SPRACHEN = [
    { kod: "de", kuerzel: "DE", name: "Deutsch", pfad: "/" },
    { kod: "en", kuerzel: "EN", name: "English", pfad: "/en/" },
    { kod: "tr", kuerzel: "TR", name: "Türkçe",  pfad: "/tr/", intern: true }
  ];

  /* YouTube-Kennungen eintragen, sobald der Kanal steht — z. B.
     ["dQw4w9WgXcQ", "..."]. Solange die Liste leer ist, bleibt der
     ganze Abschnitt verborgen: ein leerer Kasten sieht kaputt aus. */
  var VIDEOS = [];

  /* ==========================================================
     Kleinkram
     ========================================================== */

  var jahr = document.querySelector("[data-jahr]");
  if (jahr) jahr.textContent = String(new Date().getFullYear());

  /* Kopfzeile bekommt erst eine Trennlinie, wenn gescrollt wurde —
     ganz oben schwebt sie sonst ohne Grund im Bild. */
  var kopf = document.querySelector("[data-kopf]");
  if (kopf) {
    /* Gedrosselt: das Scrollereignis feuert auf einem Telefon leicht
       hundertmal pro Sekunde. Ungedrosselt schreibt jedes davon ins
       DOM und zwingt den Browser zum Nachrechnen — genau während der
       Finger wischt, also dort, wo Ruckeln am meisten auffällt. So
       wird höchstens einmal pro Bild gearbeitet.
       (Übernommen aus dem Kodozen-Gerüst.) */
    var wartet = false;
    var pruefen = function () {
      kopf.dataset.gescrollt = window.scrollY > 8 ? "ja" : "nein";
      wartet = false;
    };
    window.addEventListener("scroll", function () {
      if (wartet) return;
      wartet = true;
      if (window.requestAnimationFrame) window.requestAnimationFrame(pruefen);
      else window.setTimeout(pruefen, 60);
    }, { passive: true });
    pruefen();
  }

  var menueKnopf = document.querySelector(".menue-knopf");
  var menue = document.getElementById("hauptmenue");
  if (menueKnopf && menue) {
    var menueSetzen = function (offen) {
      menue.dataset.offen = offen ? "ja" : "nein";
      menueKnopf.setAttribute("aria-expanded", String(!!offen));
    };

    menueKnopf.addEventListener("click", function () {
      menueSetzen(menue.dataset.offen !== "ja");
    });

    /* closest("a") statt tagName: sobald in einem Menüpunkt ein <span>
       oder ein Symbol steckt, ist das Ziel des Klicks nicht mehr das
       <a> selbst, und das Menü bliebe offen stehen. */
    menue.addEventListener("click", function (e) {
      if (e.target.closest("a")) menueSetzen(false);
    });

    /* Escape schließt und gibt den Fokus zurück auf den Knopf. Ohne das
       landet die Tastatur nach dem Schließen im Nichts. */
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menue.dataset.offen === "ja") {
        menueSetzen(false);
        menueKnopf.focus();
      }
    });

    /* Wird das Telefon gedreht oder das Fenster breiter gezogen, gilt
       wieder das Menü der großen Ansicht — die aufgeklappte Fassung
       bliebe sonst als Rest im Bild stehen. */
    var breit = window.matchMedia("(min-width: 861px)");
    if (breit.addEventListener) {
      breit.addEventListener("change", function () {
        if (breit.matches) menueSetzen(false);
      });
    }

    menueSetzen(false);
  }

  /* ==========================================================
     Sprachumschalter — echte Links, damit sie ohne JavaScript
     funktionieren und Suchmaschinen ihnen folgen.
     ========================================================== */

  var sprachKasten = document.querySelector("[data-sprachen]");
  if (sprachKasten) {
    var jetzt = document.documentElement.lang || "de";
    SPRACHEN.forEach(function (s) {
      if (s.intern && s.kod !== jetzt) return;   // interne Fassung nicht anbieten
      var a = document.createElement("a");
      a.href = s.pfad;
      a.textContent = s.kuerzel;
      a.setAttribute("hreflang", s.kod);
      a.setAttribute("lang", s.kod);
      a.setAttribute("aria-label", s.name);
      if (s.kod === jetzt) a.setAttribute("aria-current", "true");
      sprachKasten.appendChild(a);
    });
  }

  /* ==========================================================
     Leistungen im Formular
     ========================================================== */

  var gitter = document.querySelector("[data-leistungen]");
  if (gitter) {
    /* Übersetzte Fassungen liefern die Liste im Kopf mit; sonst gilt
       die deutsche oben. */
    var liste = (window.CKR_LEISTUNGEN && window.CKR_LEISTUNGEN.length)
      ? window.CKR_LEISTUNGEN : LEISTUNGEN;
    liste.forEach(function (name, i) {
      var kennung = "leistung-" + i;
      var label = document.createElement("label");
      label.setAttribute("for", kennung);
      var box = document.createElement("input");
      box.type = "checkbox";
      box.id = kennung;
      box.name = "leistung";
      box.value = name;
      label.appendChild(box);
      label.appendChild(document.createTextNode(name));
      gitter.appendChild(label);
    });
  }

  /* ==========================================================
     Videos — nichts wird ungefragt geladen
     ----------------------------------------------------------
     Ein eingebetteter YouTube-Player setzt sofort Cookies. Hier
     kommt er erst auf Klick und über youtube-nocookie.com.

     Wichtiger Nachtrag: auch das Vorschaubild kam vorher von
     i.ytimg.com, also von einem Google-Server — damit wäre die
     IP-Adresse des Besuchers schon vor jedem Klick dort gelandet.
     Genau der Grund, aus dem die Schriften vom fremden Server
     geholt wurden. Deshalb erscheint ohne Zustimmung eine eigene
     Karte in Markenfarben; das echte Vorschaubild wird nur
     geladen, wenn „Externe Medien“ freigegeben ist.

     Der Klick auf eine Karte lädt dieses eine Video — eine
     bewusste Handlung des Besuchers, die gespeicherte Einstellung
     ändert er damit nicht.
     ========================================================== */

  var videoAbschnitt = document.querySelector("[data-videos]");
  var videoGitter = document.querySelector("[data-video-gitter]");
  if (videoAbschnitt && videoGitter && VIDEOS.length) {
    VIDEOS.forEach(function (id) {
      var knopf = document.createElement("button");
      knopf.type = "button";
      knopf.className = "video-karte";
      knopf.setAttribute("aria-label", "Video abspielen");

      /* Das echte Vorschaubild liegt bei Google. Ohne Freigabe
         bleibt die Karte deshalb eine eigene Fläche — sie sieht
         nicht leer aus, sie verrät nur nichts. */
      if (window.ckrEinwilligung && window.ckrEinwilligung("medien")) {
        var bild = document.createElement("img");
        bild.src = "https://i.ytimg.com/vi/" + id + "/hqdefault.jpg";
        bild.alt = "";
        bild.loading = "lazy";
        bild.width = 480; bild.height = 360;
        knopf.appendChild(bild);
      } else {
        var platz = document.createElement("span");
        platz.className = "video-karte__platz";
        platz.textContent = "Video von YouTube · zum Laden antippen";
        knopf.appendChild(platz);
      }

      var deckel = document.createElement("span");
      deckel.className = "video-karte__spiel";
      knopf.appendChild(deckel);
      knopf.addEventListener("click", function () {
        var rahmen = document.createElement("iframe");
        rahmen.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0";
        rahmen.title = "Video von CKR Cleaning Services";
        rahmen.allow = "accelerometer; autoplay; encrypted-media; picture-in-picture";
        rahmen.allowFullscreen = true;
        knopf.replaceWith(rahmen);
      });
      videoGitter.appendChild(knopf);
    });
    videoAbschnitt.hidden = false;
    var videoLink = document.querySelector("[data-videos-link]");
    if (videoLink) videoLink.hidden = false;
  }

  /* ==========================================================
     Vorher / Nachher
     ----------------------------------------------------------
     Der Regler steuert zwei Größen: wie breit das Vorher-Bild
     beschnitten wird und wie breit das Bild darin bleibt. Ohne
     das zweite würde das Motiv beim Ziehen mitwandern statt
     stehenzubleiben — dann vergleicht man zwei verschiedene
     Ausschnitte statt derselben Stelle.
     ========================================================== */

  (function () {
    var rahmen = document.querySelector("[data-vn]");
    if (!rahmen) return;
    var regler = rahmen.querySelector("[data-vn-regler]");
    var vorher = rahmen.querySelector("[data-vn-vorher]");
    if (!regler || !vorher) return;

    function zeichne() {
      var p = Number(regler.value);
      rahmen.style.setProperty("--vn", p + "%");
      /* Das innere Bild behält die Breite des Rahmens, damit der
         Bildausschnitt beim Ziehen an derselben Stelle bleibt. */
      vorher.style.setProperty("--vn-bild", p > 0 ? (10000 / p) + "%" : "10000%");
      regler.setAttribute("aria-valuetext", p + " Prozent vorher");
    }

    regler.addEventListener("input", zeichne);
    window.addEventListener("resize", zeichne);
    zeichne();
  })();

  /* ==========================================================
     Aufmacher: das Glas wird gewischt
     ----------------------------------------------------------
     Frühere Fassung koppelte das Video an den Scrollbalken. Das
     war schön gedacht und in der Praxis zerbrechlich: Springen im
     Video (seek) setzt voraus, dass der Server Bereichsabfragen
     beherrscht, dass der Browser überhaupt einen Dekoder anlegt
     und dass jeder Sprung auch ankommt. Fiel eines davon aus,
     stand das Bild still und der Besucher hing zwei Bildschirme
     lang in einem Abschnitt fest, in dem sich nichts rührte.

     Jetzt läuft das Video einfach — stumm, in Schleife, ohne
     einen einzigen Sprung. Es kann damit nicht mehr einfrieren.
     Der Abschnitt ist wieder einen Bildschirm hoch; wer scrollt,
     scrollt weiter.
     ========================================================== */

  (function () {
    var abschnitt = document.querySelector("[data-auftakt]");
    if (!abschnitt) return;

    var glas = abschnitt.querySelector(".auftakt__glas");
    if (!glas) return;

    var ruhig = window.matchMedia("(prefers-reduced-motion: reduce)");
    var schmal = window.matchMedia("(max-width: 700px)");

    /* Mit ?video=an lässt sich beides übergehen — zum Nachsehen, wenn
       jemand meldet, dass das Video nicht läuft. */
    var erzwungen = /[?&]video=an/.test(window.location.search);

    /* Warum das hier so ausführlich steht: bis hierher sind beide
       Bedingungen still ausgestiegen. Wer „Bewegung reduzieren“ im
       Betriebssystem eingeschaltet hat — unter macOS in den
       Systemeinstellungen bei Bedienungshilfen → Anzeige — bekam nie
       ein Video zu sehen, und in der Konsole stand nichts. Jede
       Verbesserung am Abspielen lief damit ins Leere, weil der Code
       gar nicht erst so weit kam. Ab jetzt sagt die Seite, warum. */
    var grund = null;
    if (ruhig.matches) {
      grund = "Im Betriebssystem ist „Bewegung reduzieren“ eingeschaltet. " +
              "Das Standbild bleibt absichtlich stehen.";
    } else if (schmal.matches) {
      grund = "Fensterbreite " + window.innerWidth + " px — bis 700 px " +
              "bleibt das Standbild stehen, damit auf dem Telefon keine " +
              "2,5 MB im Weg sind.";
    }

    if (grund && !erzwungen) {
      if (window.console) {
        console.info("[ckr] Aufmacher ohne Video: " + grund +
                     " Zum Nachsehen: ?video=an an die Adresse hängen.");
      }
      abschnitt.dataset.videoGrund = grund;

      /* Unter „Bewegung reduzieren“ wird das Video nicht von selbst
         gestartet — aber es wird auch nicht versteckt. Wer es sehen
         will, bekommt einen Knopf. Die Einstellung sagt „nichts soll
         sich ungefragt bewegen“, nicht „das darf ich nie sehen“. */
      if (ruhig.matches && !schmal.matches) {
        var knopf = document.createElement("button");
        knopf.type = "button";
        knopf.className = "knopf auftakt__video-knopf";
        knopf.textContent = "Hintergrundvideo abspielen";
        knopf.addEventListener("click", function () {
          knopf.remove();
          starten();
        }, { once: true });
        var innen = abschnitt.querySelector(".auftakt__innen");
        if (innen) innen.appendChild(knopf);
      }
      return;
    }

    starten();
  })();

  /* Die eigentliche Einrichtung steckt in einer eigenen Funktion, damit
     sie auch von Hand ausgelöst werden kann (siehe Knopf oben). */
  function starten() {
    var abschnitt = document.querySelector("[data-auftakt]");
    var glas = abschnitt && abschnitt.querySelector(".auftakt__glas");
    if (!abschnitt || !glas || glas.querySelector("video")) return;
    (function () {

    var video = document.createElement("video");
    video.muted = true;
    video.defaultMuted = true;
    video.loop = true;
    video.autoplay = true;
    video.playsInline = true;
    video.preload = "auto";
    video.setAttribute("muted", "");
    video.setAttribute("loop", "");
    video.setAttribute("autoplay", "");
    video.setAttribute("playsinline", "");
    video.setAttribute("aria-hidden", "true");
    video.tabIndex = -1;

    /* Dies ist eine Tapete, kein Videoplayer. Ohne die folgenden vier
       Zeilen behandeln Safari und Chrome die Fläche trotzdem als Player:
       ein Doppelklick geht auf Vollbild, das Betriebssystem bietet ein
       schwebendes Bild-im-Bild-Fenster an, und iOS/AirPlay wollen das
       Video auf ein anderes Gerät schicken. Alles davon reißt den
       Besucher aus der Seite heraus — genau so ist es gemeldet worden:
       das Video lief plötzlich in einem kleinen eigenen Fenster und
       nicht mehr auf der Seite. Die Schutzschicht darüber
       (pointer-events: none in styles.css) hält Klicks endgültig ab. */
    video.disablePictureInPicture = true;
    video.setAttribute("disablepictureinpicture", "");
    video.setAttribute("disableremoteplayback", "");
    video.setAttribute("x-webkit-airplay", "deny");
    video.setAttribute("controlslist", "nodownload noplaybackrate noremoteplayback nofullscreen");

    video.src = "video/glas-loop.mp4";

    /* Die Bühne muss stehen, bevor das Video eingehängt wird: in einem
       Zweig mit display:none legt der Browser keinen Dekoder an. Genau
       daran ist die alte Fassung gescheitert. */
    abschnitt.dataset.buehne = "an";
    glas.insertBefore(video, glas.firstChild);

    /* Eingeblendet wird erst, wenn wirklich ein Einzelbild gezeichnet
       wurde — nicht schon beim Ereignis „playing“. Der Unterschied ist
       gemessen worden: nach „playing“ vergingen bis zu zwei Sekunden,
       in denen der Browser immer wieder dasselbe Bild lieferte. In der
       Zeit sah das Video aus wie ein Standbild, und genau so ist es
       auch gemeldet worden. Solange nichts fließt, bleibt schlicht das
       echte Standbild stehen — das fällt niemandem auf. */
    function sichtbar() { glas.dataset.video = "bereit"; }
    if (video.requestVideoFrameCallback) {
      var gesehen = 0;
      var zaehlen = function () {
        if (++gesehen >= 2) { sichtbar(); return; }
        video.requestVideoFrameCallback(zaehlen);
      };
      video.requestVideoFrameCallback(zaehlen);
      /* Rückfall für Browser ohne diese Zählung. */
      video.addEventListener("playing", function () {
        window.setTimeout(sichtbar, 400);
      }, { once: true });
    } else {
      video.addEventListener("playing", sichtbar, { once: true });
    }

    function zurueck(grund) {
      abschnitt.removeAttribute("data-buehne");
      glas.removeAttribute("data-video");
      if (video.parentNode) video.parentNode.removeChild(video);
      if (window.console) console.warn("[ckr] Aufmacher ohne Video: " + grund);
    }

    /* Nur ein echter Ladefehler baut die Bühne ab. Abgelehntes Autoplay
       tut das ausdrücklich nicht mehr: früher verschwand dann das ganze
       Video, obwohl es beim ersten Mausklick sofort gelaufen wäre. */
    video.addEventListener("error", function () {
      zurueck("Datei fehlt oder ist defekt");
    });

    /* Manche Browser lehnen selbst stummes Autoplay ab (Energiesparmodus,
       Safari-Einstellung „Nie automatisch abspielen“, Datensparmodus).
       Dann bleibt zunächst das Standbild stehen, und die erste beliebige
       Bewegung des Besuchers löst den zweiten Versuch aus. Ein Klick auf
       das Video selbst kommt dafür nicht in Frage — die Fläche nimmt
       keine Klicks an, und das soll auch so bleiben. */
    var nachgeholt = false;

    function anstossen() {
      if (nachgeholt) return;
      var p = video.play();
      if (p && p.catch) p.catch(function () { /* weiter warten */ });
    }

    function nachholen() {
      if (nachgeholt) return;
      nachgeholt = true;
      ["pointerdown", "keydown", "wheel", "touchstart", "scroll"].forEach(
        function (art) { window.removeEventListener(art, nachholen); });
      var p = video.play();
      if (p && p.catch) {
        p.catch(function () {
          zurueck("Der Browser spielt das Video auch nach einer Eingabe nicht ab");
        });
      }
    }

    /* Wird die Seite gerade im Hintergrund vorausgeladen (Speculation
       Rules), lehnt der Browser jedes Abspielen ab — richtigerweise,
       denn niemand sieht sie. Ohne diese Abfrage würde der Fehlversuch
       als „Autoplay blockiert“ gewertet. Wir warten, bis die Seite
       wirklich aufgerufen wird. */
    if (document.prerendering) {
      document.addEventListener("prerenderingchange", function () {
        anstossen();
      }, { once: true });
      return;
    }

    var start = video.play();
    if (start && start.catch) {
      start.catch(function () {
        /* Bewusst ohne Meldung: dass ein Browser das erste automatische
           Abspielen ablehnt und es kurz darauf doch läuft, ist normales
           Verhalten und kein Fehler. Eine Warnung in der Konsole würde
           auf einer funktionierenden Seite nach einem Defekt aussehen.
           Gemeldet wird erst, wenn auch der zweite Versuch scheitert —
           dann ist das Video wirklich weg (siehe zurueck). */
        ["pointerdown", "keydown", "wheel", "touchstart", "scroll"].forEach(
          function (art) {
            window.addEventListener(art, nachholen, { once: true, passive: true });
          });
      });
    }

    /* Kommt das Fenster aus dem Hintergrund zurück, halten manche Browser
       das Video angehalten. Ein stiller Anstoß genügt. */
    document.addEventListener("visibilitychange", function () {
      if (!document.hidden && video.paused) anstossen();
    });

    /* Anfang und Ende der Aufnahme ähneln sich, aber sie sind nicht
       identisch — ohne Zutun wäre am Schleifenpunkt ein Schnitt zu
       sehen. Die letzte halbe Sekunde blendet deshalb weg und der
       Neubeginn wieder auf. */
    /* Der Schnitt am Schleifenpunkt ist in der neuen Fassung härter als
       zuvor: die Aufnahme besteht aus drei zusammengesetzten Abschnitten,
       Anfang und Ende passen nicht mehr zusammen. Eine ganze Sekunde
       Blende deckt das zu, ohne dass die Bewegung stockt. */
    var BLENDE = 1.0;
    video.addEventListener("timeupdate", function () {
      var d = video.duration;
      if (!d || !isFinite(d)) return;
      var rest = d - video.currentTime;
      var a = Math.min(video.currentTime / BLENDE, rest / BLENDE, 1);
      glas.style.setProperty("--film", a < 0 ? 0 : a);
    });
    })();
  }

  /* ==========================================================
     Einwilligung („Cookie-Banner“)
     ----------------------------------------------------------
     Zum Stand heute setzt diese Website nichts: kein Cookie, kein
     localStorage, keinen Zähler, keinen fremden Server. Die
     Schriften liegen bei uns, YouTube wird erst nach einem Klick
     geladen. Rechtlich wäre damit gar kein Banner nötig — ein
     Hinweis ist nur vorgeschrieben, wenn etwas auf dem Gerät
     gespeichert oder gelesen wird, das nicht unbedingt gebraucht
     wird.

     Er steht trotzdem hier, weil er gebraucht wird, sobald der
     Betrieb einen Zähler, eine Karte oder ein Pixel möchte. Dann
     ist die Stelle schon da und richtig gebaut, statt in Eile
     nachgerüstet zu werden.

     Vier Dinge, die die meisten Banner falsch machen:

     · „Alle akzeptieren“ groß und bunt, „Ablehnen“ klein und grau.
       Das ist keine freie Wahl und wurde in Österreich und
       Deutschland mehrfach beanstandet. Beide Knöpfe sind hier
       gleich groß und gleich erreichbar.
     · Die Wahl wird in einem Cookie gespeichert — ausgerechnet.
       Wir legen sie in den localStorage: so bleibt der Satz „diese
       Seite setzt keine Cookies“ wahr.
     · Kein Weg zurück. Im Fuß steht deshalb dauerhaft ein Link,
       der die Wahl wieder aufmacht.
     · Kategorien, die es gar nicht gibt. Hier stehen nur zwei,
       weil es nur zwei gibt. Eine dritte kommt in die Liste
       unten, sobald sie wirklich existiert.

     Wer später etwas einbindet, fragt vorher:
         if (window.ckrEinwilligung("statistik")) { ... }
     ========================================================== */

  var EINWILLIGUNG = "ckr-einwilligung";

  /* Kategorien. „notwendig“ lässt sich nicht abwählen, weil ohne sie
     nichts funktioniert — sie umfasst genau eines: das Merken dieser
     Wahl. Neue Zeile hier = neuer Schalter im Fenster. */
  var EINWILLIGUNGSARTEN = [
    { kod: "notwendig", name: "Notwendig", pflicht: true,
      text: "Speichert nur, wie Sie sich hier entschieden haben. " +
            "Ohne das würde diese Frage bei jedem Aufruf wiederkommen." },
    { kod: "medien", name: "Externe Medien", pflicht: false,
      text: "Erlaubt, dass YouTube-Videos direkt geladen werden. " +
            "Ohne diese Zustimmung erscheint zuerst ein Vorschaubild — " +
            "erst Ihr Klick lädt das Video." }
  ];

  (function () {
    function lesen() {
      try {
        var roh = window.localStorage.getItem(EINWILLIGUNG);
        return roh ? JSON.parse(roh) : null;
      } catch (e) { return null; }   /* privates Fenster, gesperrter Speicher */
    }

    function schreiben(wahl) {
      try {
        window.localStorage.setItem(EINWILLIGUNG, JSON.stringify(wahl));
      } catch (e) { /* dann gilt die Wahl eben nur für diesen Besuch */ }
      merken = wahl;
      document.documentElement.dataset.medien = wahl.medien ? "frei" : "gesperrt";
    }

    var merken = lesen();

    /* Öffentliche Abfrage für alles, was später dazukommt. */
    window.ckrEinwilligung = function (art) {
      if (art === "notwendig") return true;
      return !!(merken && merken[art]);
    };

    if (merken) {
      document.documentElement.dataset.medien = merken.medien ? "frei" : "gesperrt";
    }

    var fenster = null;

    function bauen(mitSchaltern) {
      if (fenster) fenster.remove();

      fenster = document.createElement("div");
      fenster.className = "einwilligung";
      fenster.setAttribute("role", "dialog");
      fenster.setAttribute("aria-modal", "false");
      fenster.setAttribute("aria-labelledby", "einw-titel");

      var schalter = "";
      if (mitSchaltern) {
        schalter = '<ul class="einwilligung__arten">' +
          EINWILLIGUNGSARTEN.map(function (k) {
            var an = k.pflicht || (merken && merken[k.kod]);
            return '<li><label class="einwilligung__art">' +
              '<input type="checkbox" value="' + k.kod + '"' +
              (an ? " checked" : "") + (k.pflicht ? " disabled" : "") + '>' +
              '<span><strong>' + k.name + (k.pflicht ? " (immer aktiv)" : "") +
              '</strong><br>' + k.text + '</span></label></li>';
          }).join("") + "</ul>";
      }

      fenster.innerHTML =
        '<div class="einwilligung__innen">' +
          '<h2 id="einw-titel">Ihre Entscheidung</h2>' +
          '<p>Diese Website setzt <strong>keine Cookies</strong> und misst kein ' +
          'Besucherverhalten. Gespeichert wird nur, was Sie hier auswählen. ' +
          'Mehr dazu in der <a href="' + ZUM_DATENSCHUTZ + '">Datenschutzerklärung</a>.</p>' +
          schalter +
          '<div class="einwilligung__knoepfe">' +
            '<button type="button" class="knopf" data-einw="nur">Nur notwendige</button>' +
            '<button type="button" class="knopf knopf--voll" data-einw="alle">Alle akzeptieren</button>' +
            (mitSchaltern
              ? '<button type="button" class="knopf" data-einw="auswahl">Auswahl speichern</button>'
              : '<button type="button" class="einwilligung__mehr" data-einw="mehr">Einstellungen</button>') +
          '</div>' +
        '</div>';

      document.body.appendChild(fenster);
      /* Die Handleiste am unteren Rand tritt so lange zurück; zwei
         Balken übereinander sind auf einem Telefon eine Wand. */
      document.documentElement.dataset.einwilligung = "offen";

      fenster.addEventListener("click", function (e) {
        var knopf = e.target.closest("[data-einw]");
        if (!knopf) return;
        var art = knopf.dataset.einw;

        if (art === "mehr") { bauen(true); return; }

        var wahl = { notwendig: true, medien: false, zeit: new Date().toISOString() };
        if (art === "alle") {
          wahl.medien = true;
        } else if (art === "auswahl") {
          fenster.querySelectorAll('input[type="checkbox"]:not([disabled])')
            .forEach(function (feld) { wahl[feld.value] = feld.checked; });
        }
        schreiben(wahl);
        schliessen();
      });

      /* Escape gilt als „nur notwendige“ — die zurückhaltende Wahl.
         Ein Fenster, das sich nicht schließen lässt, ist eine Falle. */
      fenster.addEventListener("keydown", function (e) {
        if (e.key !== "Escape") return;
        schreiben({ notwendig: true, medien: false, zeit: new Date().toISOString() });
        schliessen();
      });

      var ersterKnopf = fenster.querySelector("button");
      if (ersterKnopf) ersterKnopf.focus();
    }

    function schliessen() {
      if (fenster) { fenster.remove(); fenster = null; }
      delete document.documentElement.dataset.einwilligung;
    }

    /* Dauerhafter Weg zurück im Fuß — vorgeschrieben und schlicht fair:
       wer einmal zugestimmt hat, muss das zurücknehmen können. */
    var wiederOeffnen = document.querySelector("[data-einwilligung-oeffnen]");
    if (wiederOeffnen) {
      wiederOeffnen.addEventListener("click", function (e) {
        e.preventDefault();
        bauen(true);
      });
    }

    /* Beim ersten Besuch fragen. Nicht sofort: die Seite soll zuerst
       da sein, sonst ist das Erste, was jemand sieht, eine Frage. */
    if (!merken) {
      window.setTimeout(function () { bauen(false); }, 900);
    }
  })();

  /* ==========================================================
     Handleiste: Anrufen und WhatsApp, immer erreichbar
     ----------------------------------------------------------
     Der wichtigste Unterschied zwischen einem Telefon und einem
     großen Bildschirm ist nicht die Breite, sondern die Absicht.
     Wer mit dem Telefon auf der Seite einer Reinigungsfirma
     landet, hat meistens ein Problem — ein Wasserschaden, eine
     Übergabe am Freitag, ein Zimmer, das bis mittags fertig sein
     muss. Der sucht keine Leistungsübersicht, der sucht eine
     Nummer, und zwar sofort und ohne zu scrollen.

     Deshalb steht auf dem Telefon eine schmale Leiste am unteren
     Rand: anrufen, WhatsApp, Angebot. Sie ist mit dem Daumen
     erreichbar, ohne die Hand umzugreifen — die obere Bildkante
     ist es nicht.

     Zwei Feinheiten, ohne die so eine Leiste ärgert:

     · Sie verschwindet, sobald das Angebotsformular im Bild ist.
       Sonst deckt sie genau den Absendeknopf zu, auf den sie
       verweist.
     · Sie sitzt oberhalb der Systemleiste des Geräts
       (safe-area-inset-bottom). Ohne das liegt bei jedem iPhone
       der Strich für die Startgeste über den Knöpfen.

     Sie entsteht hier aus den Einstellungen ganz oben und nicht
     im HTML — so steht sie auf allen sechzehn Seiten und die
     Nummer wird an einer einzigen Stelle gepflegt. Ohne
     JavaScript fehlt sie; die Nummer steht dann weiterhin im
     Kopf und im Fuß, wie auf jeder Seite.
     ========================================================== */

  (function () {
    var schmal = window.matchMedia("(max-width: 700px)");
    if (!schmal.matches) return;

    var leiste = document.createElement("nav");
    leiste.className = "handleiste";
    leiste.setAttribute("aria-label", "Schnellkontakt");
    leiste.innerHTML =
      '<a class="handleiste__knopf handleiste__knopf--ruf" href="tel:+' + TELEFON_WA + '">' +
        '<svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true" fill="none" ' +
        'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' +
        '<path d="M6.2 2.5 8 6.1 6.3 7.9c.9 1.9 2 3 3.8 3.8l1.8-1.7 3.6 1.8v3c0 .8-.7 1.4-1.5 1.3' +
        'C7.7 15.6 4.4 12.3 2.7 4c-.1-.8.5-1.5 1.3-1.5z"/></svg>' +
        '<span>Anrufen</span></a>' +
      '<a class="handleiste__knopf" href="https://wa.me/' + TELEFON_WA + '" ' +
        'target="_blank" rel="noopener">' +
        '<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="currentColor">' +
        '<path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2m0 1.8a8.2 8.2 0 1 1-4.2 15.2' +
        'l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 0 1 12 3.8m-3.1 4c-.2 0-.5.1-.7.4-.3.3-.9.9-.9 2.1s.9 2.5 1 2.6' +
        'c.1.2 1.8 2.8 4.4 3.8 2.2.9 2.6.7 3.1.7.5 0 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.6-.3' +
        's-1.4-.7-1.6-.8c-.2-.1-.4-.1-.5.1l-.7.9c-.1.2-.3.2-.5.1-.2-.1-.9-.4-1.8-1.2-.7-.6-1.1-1.3-1.2-1.5' +
        '-.1-.2 0-.4.1-.5l.4-.5c.1-.2.2-.3.2-.5s0-.3-.1-.4c0-.1-.5-1.3-.7-1.7-.2-.4-.4-.4-.5-.4z"/></svg>' +
        '<span>WhatsApp</span></a>' +
      '<a class="handleiste__knopf handleiste__knopf--voll" href="' + ZUM_ANGEBOT + '">' +
        '<span>Angebot</span></a>';
    document.body.appendChild(leiste);
    document.documentElement.dataset.handleiste = "an";

    /* Steht das Formular im Bild, tritt die Leiste zur Seite: sie
       verdeckt sonst genau den Knopf, zu dem sie führen soll. */
    var ziel = document.querySelector("[data-formular]");
    if (ziel && window.IntersectionObserver) {
      new IntersectionObserver(function (eintraege) {
        eintraege.forEach(function (e) {
          leiste.dataset.weg = e.isIntersecting ? "ja" : "nein";
        });
      }, { threshold: 0.12 }).observe(ziel);
    }

    /* Wird das Gerät gedreht und der Bildschirm breit, gehört die
       Leiste weg — dort gibt es den Knopf oben im Kopf. */
    if (schmal.addEventListener) {
      schmal.addEventListener("change", function () {
        if (!schmal.matches) {
          leiste.remove();
          delete document.documentElement.dataset.handleiste;
        }
      });
    }
  })();

  /* ==========================================================
     Angebotsformular
     ----------------------------------------------------------
     Zwei Wege, ein Formular: E-Mail und WhatsApp. Beide bauen
     denselben Text. Kein Server nötig — das bleibt so, bis der
     Kunde ein Postfach oder ein Formularziel nennt.
     ========================================================== */

  var formular = document.querySelector("[data-formular]");
  if (!formular) return;

  var hinweis = formular.querySelector("[data-hinweis]");

  function melden(text, art) {
    if (!hinweis) return;
    hinweis.textContent = text;
    if (art) hinweis.dataset.art = art;
    else hinweis.removeAttribute("data-art");
  }

  function sammeln() {
    var d = new FormData(formular);
    var gewaehlt = d.getAll("leistung");
    return {
      email: (d.get("email") || "").trim(),
      vorname: (d.get("vorname") || "").trim(),
      nachname: (d.get("nachname") || "").trim(),
      firma: (d.get("firma") || "").trim(),
      leistungen: gewaehlt,
      anliegen: (d.get("anliegen") || "").trim()
    };
  }

  function pruefe(a) {
    if (!a.email || a.email.indexOf("@") < 1) {
      melden("Bitte geben Sie eine gültige E-Mail-Adresse an.", "fehler");
      var feld = formular.querySelector("#f-email");
      if (feld) feld.focus();
      return false;
    }
    if (!a.leistungen.length && !a.anliegen) {
      melden("Bitte wählen Sie eine Leistung oder beschreiben Sie Ihr Anliegen.", "fehler");
      return false;
    }
    return true;
  }

  function textBauen(a) {
    var z = [];
    var name = (a.vorname + " " + a.nachname).trim();
    if (name) z.push("Name: " + name);
    if (a.firma) z.push("Firma: " + a.firma);
    z.push("E-Mail: " + a.email);
    if (a.leistungen.length) z.push("Leistungen: " + a.leistungen.join(", "));
    if (a.anliegen) z.push("", "Anliegen:", a.anliegen);
    return z.join("\n");
  }

  formular.addEventListener("submit", function (e) {
    e.preventDefault();
    var a = sammeln();
    if (!pruefe(a)) return;
    var betreff = "Angebotsanfrage" + (a.firma ? " — " + a.firma : "");
    window.location.href = "mailto:" + EMAIL +
      "?subject=" + encodeURIComponent(betreff) +
      "&body=" + encodeURIComponent(textBauen(a));
    melden("Ihr E-Mail-Programm wurde geöffnet. Bitte dort noch absenden.", "gut");
  });

  var waKnopf = formular.querySelector('[data-senden="whatsapp"]');
  if (waKnopf) {
    waKnopf.addEventListener("click", function () {
      var a = sammeln();
      if (!pruefe(a)) return;
      var url = "https://wa.me/" + TELEFON_WA + "?text=" +
        encodeURIComponent("Angebotsanfrage\n\n" + textBauen(a));
      window.open(url, "_blank", "noopener");
      melden("WhatsApp wurde geöffnet. Bitte dort noch absenden.", "gut");
    });
  }
})();
