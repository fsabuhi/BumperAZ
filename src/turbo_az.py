from bs4 import BeautifulSoup
import requests
import mechanize

def link_generator(model_id):
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    br.open("https://turbo.az")
    br.select_form(name="q_form")
    br.find_control(name='q[model][]',nr=1).get('{}'.format(model_id)).selected=True
    #br.find_control(name='q[make][]').get('{}'.format(marka_id)).selected=True
    # br.find_control(name='q[color][]',nr=1).get('{}'.format('')).selected=True
    # br.find_control(name='q[fuel_type][]',nr=1).get('{}'.format('')).selected=True
    # br.find_control(name='q[year_from][]').get('{}'.format('')).selected=True
    # br.find_control(name='q[year_to][]').get('{}'.format('')).selected=True
    br.submit()
    link = br.geturl()
    return link

def get_advertisement_links(url,count=None):
    """
    returns links. returns 3 link if no count provided.
    """
    links = []
    site= requests.get(url)
    soup = BeautifulSoup(site.content, 'html.parser')
    cars = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['products-i'])
    if count:
        init_count=count
    else:
        init_count = 3
    count = init_count if len(cars) >= init_count else len(cars)
    for i in range(count):
        i = cars[i]
        links.append('https://turbo.az'+i.find('a',class_="products-i__link").attrs['href'])
    return links

def get_advertisement_info(url,proxy):  
    """
    Returns dict with keys (title,images,car_details,car_price,additional_info,car_functions)
    """
    result = {}
    site = requests.get(url,proxies=proxy,headers={'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
)
    print(site.status_code,site.reason)
    if site.status_code == 429:
        import sys
        sys.exit("429!! too many requests")

    soup = BeautifulSoup(site.content, 'html.parser')

    result['title'] = soup.find_all('div',class_='page-content')[0].find_all('h1',class_='product-title')[0].text
    result['publish_date'] = soup.find_all('ul',class_='product-statistics')[0].find_all('span',class_='product-statistics__i-text')[0].text
    details=[]
    
    result['images']= []
    
    #self.img = soup.find_all('img',class_='product-photos__slider-top')
    for i in range(4):
        result['images'].append(soup.find_all('div',class_='product-photos__slider-top-i')[i].find_all('img')[0].attrs['src'])    
    info = soup.find_all('section',class_="product-section product-section--wide")
    
    result['car_price'] = soup.find_all('div',class_="product-price")[0].text
    
    details_name=info[0].find_all('label',class_='product-properties__i-name')
    details_value=info[0].find_all('span',class_='product-properties__i-value')
    for i in range(len(details_name)):
        details.append(details_name[i].text+': '+details_value[i].text)
    
    result['car_details']= '\n'.join(details)
    #result['car_price']= self.price
    try:
        result['additional_info']=info[1].find('p').text
    except AttributeError:
        result['additional_info'] = ""
    result['car_functions']=info[2].get_text(separator=', ')
    return result

