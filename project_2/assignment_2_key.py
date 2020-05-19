import requests
from lxml import html
from urllib.parse import urljoin


top_movies = []


def scrape(pageURL):
    resp = requests.get(url=pageURL, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    })

    tree = html.fromstring(html=resp.text)
    movies = tree.xpath("//div[@class='lister-item-content']")

    for movie in movies:
        m = {
            'title': movie.xpath(".//h3/a/text()")[0],
            'year of release': movie.xpath(".//h3/span[contains(@class, 'lister-item-year')]/text()")[0],
            'duration': movie.xpath(".//p/span[@class='runtime']/text()")[0],
            'rating': movie.xpath(".//div[@class='ratings-bar']/div[@name='ir']/@data-value")[0]
        }
        top_movies.append(m)

    next_page = tree.xpath("//div[@class='desc']/a[contains(text(), 'Next')]/@href")

    if len(next_page) != 0:
        scrape(pageURL=urljoin(base=pageURL, url=next_page[0]))
    else:
        return


scrape(pageURL='https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc')
#print(top_movies)
print(len(top_movies))