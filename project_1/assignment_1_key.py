import requests
from lxml import html
import json


def write_to_json(products):
    with open('products.json', 'w') as f:
        f.write(json.dumps(products))

all_products = []

#Response object
resp = requests.get(url='https://www.ebay.com/trending', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
})

#Element Tree object
tree = html.fromstring(html=resp.text)

#Get trending items
trending_items = tree.xpath("//div[contains(@id, 'topic')]/div[@class='topic-container']")

for trending_item in trending_items:
    item = {
        'name': trending_item.xpath(".//h2[@class='title']/a/text()")[0],
        'url': trending_item.xpath(".//h2[@class='title']/a/@href")[0],
        'info': trending_item.xpath(".//div[@class='info']/p/text()")[0],
        'searches': trending_item.xpath(".//div[@class='info']/div[@class='graph']/div[@class='stats']/div/strong/text()")[0]
    }

    all_products.append(item)

print(all_products)

write_to_json(all_products)