from attr import attrs
from bs4 import BeautifulSoup
import re

f = open("demofile2.txt", "r")
html = f.read()
f.close()

soup = BeautifulSoup(html, 'html5lib')

items = []

table = soup.find_all('div', attrs={"class":"s-item__info clearfix"})

def get_text(node):
    try:
        res = node.text
        return res
    except:
        return 'NA'

for row in table:
    item = {}

    item['title'] = get_text( row.find('h3', attrs = {"class":"s-item__title"}))
    item['price'] = get_text(row.find('span', attrs = {"class":"s-item__price"}).find('span', attrs = {"class" : "POSITIVE"}))
    item['bids'] = get_text(row.find('span', attrs = {"class": "s-item__bids"}))
    

print(items)