from bs4 import BeautifulSoup
import requests
import sys

link = sys.argv[1]

page = requests.get(link).content
soup = BeautifulSoup(page, 'html.parser')

print("Title:", soup.title.string)

# print(soup.get_text())
# print(soup.find_all("div", attrs={"drop-cap-letter":True}))
# for i in soup.find_all("p", attrs={"data-el": "text"}): print(i)

# print(soup.find_all("p"))

# for p in soup.select(".font--article-body"):
#     print(p.text)

print(" ".join([i.text for i in soup.select(".font--article-body")]))
