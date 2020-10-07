import requests
from bs4 import BeautifulSoup

fravega_site = "https://www.fravega.com"

results = requests.get(fravega_site)

src = results.content

soup = BeautifulSoup(src, "lxml")

categoryItem_li = soup.find_all(attrs={"name": "CategoryItem"})
categoryItem_list = []
for a_tag in categoryItem_li:
    categoryItem_list.append((a_tag.find("a"))["href"])

subcategory_links = []

for item in categoryItem_list:
    results = requests.get(categoryItem_list[2])
    src = results.content
    soup = BeautifulSoup(src, "lxml")
    cajas = soup.find_all("div", class_="cajas")
    columna = []
    for col in cajas:
        columna = col.find_all("h3")
        for a_tag in columna:
            subcategory_links.append(fravega_site + a_tag.find("a")["href"])

print(subcategory_links)