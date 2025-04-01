from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine

# Set path to ChromeDriver (Replace this with the correct path)
CHROMEDRIVER_PATH = "C:/Users/iamth/Downloads/chromedriver-win64-2/chromedriver-win64/chromedriver.exe"

# Initialize WebDriver with Service
service = Service(CHROMEDRIVER_PATH)
options = webdriver.ChromeOptions()

options.add_argument("--window-size=1920,1080")  # Set window size
options.add_argument("--disable-blink-features=AutomationControlled")

choice = "yes"
while choice == "yes":
    search = input('Type search: ').replace(" ", "+")

    driver = webdriver.Chrome(service=service, options=options)

    # Open Google Search URL
    search_url = "https://www.google.com/search?q=" + search +"&oq=" + search

    driver.get(search_url)

    # Wait for the page to load
    time.sleep(2)

    page_html = driver.page_source

    soup = BeautifulSoup(page_html,'html.parser')
    obj={}
    l=[]
    allData = soup.find("div",{"class":"dURPMd"}).find_all("div",{"class":"Ww4FFb"})
    for i in range(0,len(allData)):
        try:
            obj["title"]=allData[i].find("h3").text
        except:
            obj["title"]=None

        try:
            obj["link"]=allData[i].find("a").get('href')
        except:
            obj["link"]=None

        try:
            obj["description"]=allData[i].find("div",{"class":"VwiC3b"}).text
        except:
            obj["description"]=None

        #add object to database
        l.append(obj)
        obj={}

    df = pd.DataFrame(l)
    df.to_csv('google/csv/' + search +'_google.csv', index=False, encoding='utf-8')

    # add to postgres
    engine = create_engine("postgresql+pg8000://postgres:postgres@localhost:5432/postgres")
    df.to_sql("search_results", engine, schema="google_scraper", if_exists="append", index=False)

    with open("google/html/"+ search +".html", "w", encoding="utf-16") as file:
        file.write(df.to_html(border=1))

    driver.quit()

    print("Data saved to PostgresSQL database in google_scrapes schema!\n" + search)

    choice = input("Do you want to continue (yes/no)")

print("Bye!")