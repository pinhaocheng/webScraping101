import requests
from fake_useragent import UserAgent
import json
from urllib.parse import urljoin
import sqlite3

ua = UserAgent()

extracted_products =[]

def scrapper(pageNumber=1):
    url = "https://www.walgreens.com/productsearch/v1/products/search"

    querystring = {"instart_disable_injection":"true"}

    payload = {"p":2,"s":24,"view":"allView","geoTargetEnabled":False,"abtest":["tier2","showNewCategories"],"deviceType":"desktop","id":["350006"],"requestType":"tier3","sort":"Top Sellers","couponStoreId":"10408"}
    headers = {
    'Content-Type': 'application/json',
    'User-Agent': ua.random
    }

    response = requests.post(url, headers=headers, data = json.dumps(payload), params=querystring)

    data = response.json()

    try:
        products = data['products']

        for product_info in products:
            pr_info = product_info['productInfo']
            pr = {
                'img': pr_info['imageUrl'],
                'price': pr_info['priceInfo']['regularPrice'],
                'id': pr_info['prodId'],
                'name': pr_info['productDisplayName'],
                'size': pr_info['productSize'],
                'url': urljoin(base='https://walgreens.com', url=pr_info['productURL'])
            }
            extracted_products.append(pr)
        
        pageNumber += 1
        scrapper(pageNumber=pageNumber)
    except KeyError:
        return

scrapper()

connection = sqlite3.connect("walgreens.db")
try:
    c = connection.cursor()
    c.execute('''
        CREATE TABLE products (
            id TEXT PRIMARY KEY,
            name TEXT,
            url TEXT,
            size TEXT,
            price TEXT,
            image TEXT
        )
    ''')
    connection.commit()
except sqlite3.OperationalError as e:
    print(e)

for product in extracted_products:
    try:
        c.execute('''
            INSERT INTO products (id, name, url, size, price, image) VALUES (
                ?,?,?,?,?,?
            )
        ''', (
            product['id'],
            product['name'],
            product['url'],
            product['size'],
            product['price'],
            product['img']
        ))
    except sqlite3.IntegrityError:
        pass
 
connection.commit()
connection.close()