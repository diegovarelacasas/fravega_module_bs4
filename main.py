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
fravega_category_sublink = "https://www.fravega.com/l/?categorias="

soup = getsoup(fravega_site)
categoryItem_list = soup.select("[name=CategoryItem] > a")              # Get the category Item Li
categoryItem_links = [link["href"] for link in categoryItem_list]       # get every link on the li category Item list

subcategory_links = []

for category in categoryItem_links:                                      #serch every link on every subcategory item
    soup = getsoup(category)
    subcategory_list = soup.select("div.cajas h3 a")
    for link in subcategory_list:
        if "=" in link["href"]:   #  if the format is "https://www.fravega.com/l/?categorias="
            href_link = link["href"][link["href"].find("=")+1:]  #use only text after = caracter
            if href_link.find("/") == -1:  # evaluate if the href_link does´n end in a /
                subcategory_links.append(fravega_category_sublink + href_link)
            else:
                subcategory_links.append(fravega_category_sublink + href_link[:href_link.find("/")])
        elif link["href"].startswith("/l/"):    # if the subcategory has the format "https://www.fravega.com/l/tv-y-video/tv/"
            href_link = link["href"][link["href"].find("/l/")+3:]
            if href_link.find("/") == -1:  # evaluate if the href_link does´n end in a /
                subcategory_links.append(fravega_category_sublink + href_link)
            else:
                subcategory_links.append(fravega_category_sublink + href_link[:href_link.find("/")])
        elif link["href"] != "":  ## format /seguridad-para-el-hogar/ and not black
            href_link = link["href"][1:]
            subcategory_links.append(fravega_category_sublink + href_link[:href_link.find("/")])


subcategory_links = list(OrderedDict.fromkeys(subcategory_links))

#print(subcategory_links)
"""
product_link = []

for subcategory in subcategory_links:
    soup = getsoup(subcategory)
    itemGrid = soup.select("[name=itemsGrid] > li a")
    for item in itemGrid:
        if item["href"] not in product_link:
            product_link.append("https://www.fravega.com" + item["href"])

print(product_link)
print(len(product_link))
"""

product_links = []

for category in subcategory_links:
    current_page = 1
    next_page_enable = True
    while next_page_enable:
        next_page_enable = False
        soup = getsoup(category+ "&page="+ str(current_page))
        itemGrid = soup.select("[name=itemsGrid] > li a")
        for item in itemGrid:
            product_links.append(item["href"])
            print(item["href"])
        next_page = soup.select("[class=ant-pagination] > li")
        for button in next_page:
            if button["title"] == "Next Page" and button["aria-disabled"] == "false":
                current_page += 1
                next_page_enable = True

print(len(product_links))


#print(next_page[8]["title"])


#name = itemGrid[0].find("h4").getText()
#link = "https://www.fravega.com" + itemGrid[0]["href"]



#product1 = product(name,link)


#print(product1.fulldata())


