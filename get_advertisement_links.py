from bs4 import BeautifulSoup
import requests
import re
class get_advertisement_links:
    def __init__(self,url,count=None):
        site= requests.get(url)
        soup = BeautifulSoup(site.content, 'html.parser')
        cars = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['products-i'])
        self.urls=[]
        if count:
            init_count=count
        else:
            init_count = 3
        count = init_count if len(cars) >= init_count else len(cars)
        for i in range(count):
            i = cars[i]
            self.urls.append('https://turbo.az'+i.find('a',class_="products-i__link").attrs['href'])

