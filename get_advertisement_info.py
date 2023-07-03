from bs4 import BeautifulSoup
import requests
class get_advertisement_info:
    def __init__(self,url):  
        site= requests.get(url)
        soup = BeautifulSoup(site.content, 'html.parser')
        self.title = soup.find_all('div',class_='page-content')[0].find_all('h1',class_='product-title')[0].text
        details=[]
        self.images= []
        #self.img = soup.find_all('img',class_='product-photos__slider-top')
        for i in range(4):
            self.images.append(soup.find_all('div',class_='product-photos__slider-top-i')[i].find_all('img')[0].attrs['src'])    
        info = soup.find_all('section',class_="product-section product-section--wide")
        self.price = soup.find_all('div',class_="product-price")[0].text
        details_name=info[0].find_all('label',class_='product-properties__i-name')
        details_value=info[0].find_all('span',class_='product-properties__i-value')
        for i in range(len(details_name)):
            details.append(details_name[i].text+': '+details_value[i].text)
        self.car_details= '\n'.join(details)
        self.car_price = self.price
        self.additional_info=info[1].find('p').text
        self.car_functions=info[2].get_text(separator=', ')
