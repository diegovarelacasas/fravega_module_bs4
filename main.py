import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import re

def getsoup(url):
    results = requests.get(url)
    src = results.content
    return BeautifulSoup(src, "lxml")

class product:

    def __init__(self, name, link):
        self.name = name
        self.link = link

    def fulldata(self):
        return "name: " + self.name + "|" + "link: " + self.link

fravega_site = "https://www.fravega.com"

soup = getsoup(fravega_site)
categoryItem_list = soup.select("[name=CategoryItem] > a")              # Get the category Item Li
categoryItem_links = [link["href"] for link in categoryItem_list]       # get every link on the li category Item list

subcategory_links = []

for category in categoryItem_links:                                      #serch every link on every subcategory item
    soup = getsoup(category)
    subcategory_list = soup.select("div.cajas h3 a")
    for link in subcategory_list:
        if link["href"] not in subcategory_links:   #remove duplicates
            subcategory_links.append(fravega_site + link["href"])
            print(link["href"])
#print(subcategory_links)

sub2 = subcategory_links[0]


#print('\n'.join(map(str, subcategory_links)))
"""
product_link = []

for subcategory in subcategory_links:
    soup = getsoup(subcategory)
    itemGrid = soup.select("[name=itemsGrid] > li a")
    for item in itemGrid:
        if item["href"] not in product_link:
            product_link.append("https://www.fravega.com" + item["href"])

print(product_link)
"""



#soup = getsoup("https://www.fravega.com/l/?categorias=tv-y-video")

#itemGrid = soup.select("[name=itemsGrid] > li a")

#name = itemGrid[0].find("h4").getText()
#link = "https://www.fravega.com" + itemGrid[0]["href"]

#product1 = product(name,link)

#print(product1.fulldata())


