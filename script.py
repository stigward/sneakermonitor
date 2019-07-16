import os
import sys
import json
import requests
import datetime
import time
import re

from bs4 import BeautifulSoup as bs


inStockList = []

def get_current_in_stock(session):
    global inStockList
    endpoint = "https://www.nike.com/launch/?s=in-stock"
    response = session.get(endpoint)
    soup = bs(response.text, "html.parser")
    cards = soup.find_all("figure", {"class":"pb2-sm va-sm-t ncss-col-sm-6 ncss-col-md-3 ncss-col-xl-2 prl1-sm"})
    for i in cards:
        if "aria-label" in str(i):
            arr = re.split("data-qa=",str(i))
            name = re.split("aria-label=| class", arr[1])
            inStockList.append(name[2])



def refresher(session):
    while(1):
        stock = inStockList
        get_current_in_stock(session)
        for i,v in enumerate(stock):
            if v != inStockList[i]:
                print("difference found!")
                return inStockList[i]
            else:
                print("no difference. Continuing...")
                time.sleep(5)



def main():
    session = requests.session()
    refresher(session)

main()