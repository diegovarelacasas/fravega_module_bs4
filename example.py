import requests
from bs4 import BeautifulSoup

results = requests.get("https://www.whitehouse.gov/briefings-statements/")

src = results.content
soup = BeautifulSoup(src, "lxml")

urls = []
for h2_tags in soup.find_all("h2"):
    a_tag = h2_tags.find("a")
    urls.append(a_tag.attrs["href"])
print(urls)
