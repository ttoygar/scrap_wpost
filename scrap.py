from bs4 import BeautifulSoup
import requests
import sys

link = sys.argv[1]

page = requests.get(link).content
soup = BeautifulSoup(page, 'html.parser')

print("Title:", soup.title.string)

print(" ".join([i.text for i in soup.select(".font--article-body")]))
