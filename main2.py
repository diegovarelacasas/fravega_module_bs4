import requests
from bs4 import BeautifulSoup

fravega_site = "https://www.fravega.com"

results = requests.get(fravega_site)
src = results.content
soup = BeautifulSoup(src, "lxml")

categoryItem_list = soup.select("[name=CategoryItem] > a")              # Get the category Item Li
categoryItem_links = [link["href"] for link in categoryItem_list]       # get every link on the li category Item list

subcategory_links = []

for category in categoryItem_links:                                      #serch every link on every category item
    results = requests.get(category)
    src = results.content
    soup = BeautifulSoup(src, "lxml")
    subcategory_list = soup.select("div.cajas h3 a")
    for link in subcategory_list:
        subcategory_links.append(fravega_site + link["href"])

print(subcategory_links)