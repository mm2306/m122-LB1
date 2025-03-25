# m122-LB1
Google Scraper

Kurzfassung
Als eine der grössten Suchmaschinen enthält Google enorme Daten, die für Unternehmen und Forscher wertvoll sind.

Um jedoch die Google-Suchergebnisse effizient und effektiv abzurufen, muss Ihre Datenpipeline robust und skalierbar sein und dynamische Änderungen in der Google-Struktur verarbeiten können.

In diesem README werden wir einen Google-Suchergebnis-Scraper von Grund auf mit Python und der BeautifulSoup-Bibliothek erstellen, der es Ihnen ermöglicht, die Datenextraktion zu automatisieren und umsetzbare Erkenntnisse aus den Daten der Suchmaschine zu gewinnen.

Ziel ist dann diese Daten auf einer PostgreSQL Datenbank abzuspeichern.

1 Nötige Hilfsmittel
Um dieses Programm zu machen benötigt man über eine Internetverbindung, einem Python Compiler und einem funktionstüchtigen Laptop.

2 Vorgehen

2.1 Ordner und File erstellen
Als erstes erstellt man einen Ordner um die Python-Scripts darin zu speichern. Danach haben wir Source-Code der vorgegebenen Webseite entnommen.
https://www.scrapingdog.com/blog/scrape-google-search-results/
Danach mussten wir anhand des folgendem Befehl die Library herunterladen: 
-	pip install beautifulsoup4 selenium pandas

2.2 Chromedriver herunterladen
Als nächsten Schritt lädt man den Chromedriver herunter. Dies findet man online unter diese Adresse:
https://developer.chrome.com/docs/chromedriver/downloads?hl=de

2.3 CSV-Datei gemäss Input erstellen
