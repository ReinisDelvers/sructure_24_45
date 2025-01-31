# get alot of data from ss.lv
import requests
import os
from bs4 import BeautifulSoup as bs
import csv
import time

URL = "https://www.ss.lv/lv/transport/cars/today-5/sell/"
DATA = "masinmacisanas/data/"
PAGES = "masinmacisanas/pages/"

def save_page(url, name):
    gotted = requests.get(url)
    print(gotted.status_code)
    if gotted.status_code == 200:
        with open(name, "w", encoding="utf-8") as f:
            f.write(gotted.text)
    return

def save_all_pages(number):
    for i in range(1, number+1):
        save_page(f"{URL}page{i}.html", f"{PAGES}lapa{i+280}.html")
        time.sleep(1)

def get_info(page):
    data = []
    replace1 = str.maketrans({"D": "", "E": "", "H": "", "B": ""})
    replace2 = str.maketrans({".": "", "0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": ""})
    replace3 = str.maketrans({"t": "", "ū": "", "k": "", "s": "", "t": "", ".": ""})
    replace4 = str.maketrans({",": "", "€": ""})
    with open(page, "r", encoding="utf-8") as f:
        html = f.read()
    soup = bs(html, "html.parser")
    important = soup.find(id="page_main")
    tables = important.find_all("table")
    lines = tables[2].find_all("tr")
    for line in lines[1:-1]:
        fields = line.find_all("td")
        if len(fields)<8:
            print("Wierd line")
            continue
        auto = {}
        auto["advertisment_site"] = fields[1].find("a")["href"]
        auto["image"] = fields[1].find("img")["src"]

        auto["marka"] = fields[3].get_text()
        auto["gads"] = int(fields[4].get_text())
        Volume = 0
        try:
            if fields[5].get_text().translate(replace2) == "E":
                Volume = 0
            Volume = float(fields[5].get_text().translate(replace1))
        except:
            Volume = None
        auto["tilpums"] = Volume
        Type = ""
        try:
            Temp = fields[5].get_text().translate(replace2)
            if Temp == "D":
                Type = 1
            if Temp == "E":
                Type = 2
            if Temp == "H":
                Type = 3
            if Temp == "B":
                Type = 4

        except:
            Type = ""
        auto["tips"] = Type
        Mileage = 0
        try:
            Mileage = int(fields[6].get_text().translate(replace3))*1000
        except:
            Mileage = None
        auto["nobraukums"] = Mileage
        Price = 0
        try:
            Price = int(fields[7].get_text().translate(replace4))
        except:
            Price = None
        auto["cena"] = Price
        data.append(auto)
    return data
        
def save_data(data):
    with open(DATA+"sslv.csv", "w", encoding="utf-8") as f:
        field_name = ["advertisment_site", "image", "marka", "gads", "tilpums", "tips", "nobraukums", "cena"]
        w = csv.DictWriter(f, fieldnames=field_name)
        w.writeheader()
        for auto in data:
            w.writerow(auto)
        return

def get_all_info(number):
    all_data = []
    for i in range(1, number+1):
        data = get_info(f"{PAGES}lapa{i}.html")
        all_data += data
    return all_data

# save_all_pages(277)
#280 277
save_data(get_all_info(557))