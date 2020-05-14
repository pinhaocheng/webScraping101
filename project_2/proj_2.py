import requests
from lxml import html
from urllib.parse import urljoin

# to take care of empty results 
def get(list_elements):
    try:
        return list_elements.pop(0)
    except:
        return ''
 
all_movies = []
 
def scrape(url):
    resp = requests.get(url=url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    })
 
    tree = html.fromstring(html=resp.content)
    movies = tree.xpath("//div[@class='lister-item mode-advanced']/div[3]")
 
    for movie in movies:
        m = {
            'title': get(movie.xpath(".//h3/a/text()")),
            'year of release': get(movie.xpath("h3/span[@class='lister-item-year text-muted unbold']/text()")),
            'duration': get(movie.xpath(".//p/span[@class='runtime']/text()")),
            'rating': get(movie.xpath(".//div[@class='ratings-bar']/div[@name='ir']/@data-value"))
        }
        all_movies.append(m)
    
    next_page = tree.xpath("(//a[@class='lister-page-next next-page']/@href)[1]")
 
    if len(next_page) != 0:
        next_page_url = urljoin(base=url, url=next_page[0])
        scrape(url=next_page_url)
 
scrape(url="https://www.imdb.com/search/title/?genres=drama&groups=top_250&sort=user_rating,desc&ref_=adv_prv")
print(len(all_movies))