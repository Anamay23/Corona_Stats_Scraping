import requests
import time
from bs4 import BeautifulSoup
import schedule
from spreadsheet import *

def scrape():

    url = 'https://www.mohfw.gov.in/'
    response = requests.get(url)
    #print(response)
    soup = BeautifulSoup(response.text, 'html.parser')

    dbody = soup('div', {"class": "site-stats-count"})[0].find_all('li')

    num = []
    for number in dbody:
        n = number.contents[3].get_text()
        num.append(n)

    # pop some unrequired data and convert list from string to int
    num.pop(4)
    #print(num)

    num = [int(i) for i in num]

    # create proper recovered cases number (recovered+migrated)
    numRec = num[1]+num[3]

    activeCases = num[0]
    recoveries = numRec
    deaths = num[2]

    gsheet_store(activeCases, recoveries, deaths)

#schedule.every(5).seconds.do(scrape)
print("doing")
schedule.every().day.at("03:30").do(scrape) #9:00 am IST is 3:30 am UTC
print("done")

while True:
    schedule.run_pending()
    time.sleep(1)
