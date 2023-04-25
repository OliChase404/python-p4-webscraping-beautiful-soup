from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://www.npr.org/2023/04/25/1171924186/contact-is-lost-with-a-japanese-spacecraft-attempting-to-land-on-the-moon", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')

article_text = (doc.select("p"))

# for p in article_text:
#     print(p.text)



name = doc.select(".storytitle")[0].name

print(name)


attrs = doc.select(".storytitle")[0].attrs

print(attrs)