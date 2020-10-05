import requests
from bs4 import BeautifulSoup

results = requests.get("http://www.google.com")

#print(results.status_code)

#print(results.headers)

src = results.content
#print(src)

soup = BeautifulSoup(src, "lxml")

links = soup.find_all("a")
#print(links)
for link in links:
    if "acerca" in link.text:
        print(link)
        print(link.attrs["href"])
