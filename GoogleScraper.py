from selenium import webdriver

from selenium.webdriver.chrome.service import Service

import time

from bs4 import BeautifulSoup

import pandas as pd

from sqlalchemy import create_engine

# Get search term from user
search = input('Type search: ').replace(" ", "+")
search_url = f"https://www.google.com/search?q={search}&oq={search}"

# Set path to ChromeDriver
CHROMEDRIVER_PATH = "C:/Users/iamth/Downloads/chromedriver-win64-2/chromedriver-win64/chromedriver.exe"
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")

# Remove headless mode for testing
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)
driver.get(search_url)

# Increase wait time
time.sleep(5)

page_html = driver.page_source
soup = BeautifulSoup(page_html, 'html.parser')
results = []

# Updated selector for search results
search_results = soup.find_all("div", {"class": "g"})

if search_results:
    print(f"Number of results found: {len(search_results)}")
    for item in search_results:
        result = {}
        try:
            result["title"] = item.find("h3").text

        except:
            result["title"] = None

        try:
            result["link"] = item.find("a")["href"]

        except:
            result["link"] = None

        try:
            # Updated selector for description
            result["description"] = item.find("div", {"class": "VwiC3b"}).text.strip()

        except:
            result["description"] = None

        if result["title"] or result["link"] or result["description"]:
            results.append(result)

else:
    print("No results found!")

df = pd.DataFrame(results)
print(df)

# Save to CSV
df.to_csv(f'{search}_google.csv', index=False, encoding='utf-8')
print(f"Data saved to {search}_google.csv")

# Save to PostgreSQL
engine = create_engine("jdbc:postgresql://localhost:5432/postgres")
df.to_sql("search_results", engine, schema="google_scrapes", if_exists="append", index=False)

print("Data saved to PostgresSQL database in google_scrapes schema!")
driver.quit()
