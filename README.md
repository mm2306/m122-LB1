m122-LB1
Google Scraper

Kurzfassung

Als eine der grössten Suchmaschinen enthält Google enorme Daten, die für Unternehmen und Forscher wertvoll sind.

Um jedoch die Google-Suchergebnisse effizient und effektiv abzurufen, muss Ihre Datenpipeline robust und skalierbar sein und dynamische Änderungen in der Google-Struktur verarbeiten können.

In diesem README werden wir einen Google-Suchergebnis-Scraper von Grund auf mit Python und der BeautifulSoup-Bibliothek erstellen, der es Ihnen ermöglicht, die Datenextraktion zu automatisieren und umsetzbare Erkenntnisse aus den Daten der Suchmaschine zu gewinnen.

Ziel ist dann diese Daten auf einer PostgreSQL Datenbank abzuspeichern.

1 Nötige Hilfsmittel Um dieses Programm zu machen benötigt man über eine Internetverbindung, einem Python Compiler und einem funktionstüchtigen Laptop.

2 Vorgehen

2.1 Ordner und File erstellen Als erstes erstellt man einen Ordner um die Python-Scripts darin zu speichern. Danach haben wir Source-Code der vorgegebenen Webseite entnommen. https://www.scrapingdog.com/blog/scrape-google-search-results/ Danach mussten wir anhand des folgendem Befehl die Library herunterladen:

pip install beautifulsoup4 selenium pandas
2.2 Chromedriver herunterladen Als nächsten Schritt lädt man den Chromedriver herunter. Dies findet man online unter diese Adresse: https://developer.chrome.com/docs/chromedriver/downloads?hl=de

2.3 CSV-Datei gemäss Input erstellen

Im bereits vorgegebenen Code hat man mit diesem Zustand bereits die CSV-Dateien. Falls dies nicht funktioniert, muss man kontrollieren, ob man alle imports mit pip install heruntergeladen hat.

2.4 Ergebnisse auf DB speichern

Nachdem man die CSV-Datei erstellt, kann man nun auch noch die Ergebnisse in einer Datenbank als Tabelle speichern. Dazu braucht man ein Docker-Server mit einer Postgres-Datenbank welche man mit folgendem Command im CMD oder im Terminal erstellen kann:

docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:latest

Danach muss man mit pip install sqlalchemy ein DB-Toolkit herunterladen um ein engine zu erstellen, welcher auf die Prostgres-DB zugreifen kann. Danach kann man mit .to_sql die Objekte in einer Tabelle einfügen.

2.5 HTML Tabelle erstellen

Dies geht genauso wie die CSV Datei. Jedoch öffne ich mit der with open funktion ein file. Ich nutzte das utf-16 als encoding. Man öffnet somit eine HTML-Datei und dort schreibt man das Dataframe mit der .to_html Funktion auf.

2.6 Vorgegebener Code erklärt

Nachdem man mit dem installierten Driver ein Fenster öffnet, kopiert man diese Seite in ein Object. Die h3-Tags werden als Titel gezählt, während die a-Tags als Link und p-Tags die Beschreibung sind. Diese Objekte werden in einem Array gespeichert. Dieser Array wird als Dataframe gespeichert, welcher man dann zu einem CSV/eeiner Tabelle umwandeln kann.

3 Fazit

Ich lernte in diesem Projekt, wie man mit einem Auftrag sich weitere Kenntnisse beibringen kann. Ich hatte schon wenig Erfahrung mit Python und konnte wegen dem im Rahmen des Auftrag schnell verstehen, wie der Code funktioniert. Ich konnte meine Kenntnisse mit Datenbanken gebrauchen um die Ergebnisse in eine Datenbank einzufügen. Danach war es selbsterklärend, wie dies mit dem HTML funktioniert. Ich finde es passend, wie grosse Fortschritte ich machen konnte. Für das nächste Mal würde ich berücksichtigen, dass ich den Code schöner schreiben würde. Dieser ist jetzt noch eher unleserlich, aber funktionell.