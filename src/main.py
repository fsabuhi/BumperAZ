class get_cars:
    def __init__(self,model):
        from turbo_az import get_advertisement_info as info
        from turbo_az import get_advertisement_links as ads
        from turbo_az import link_generator as link
        from id_generator import id_generator as id
        car = id(model)
        brand_id = car['brand_id']
        model_id = car['model_id']
        link = link(model_id)
        ads_links = ads(link)     
        cars=[]
        images=[]
        self.ads_count=len(ads_links)
        for i in ads_links:
            data = info(i)
            cars.append('{}\n{}\n{}'.format(data['car_details'],data['car_price'],i))
            images.append(data['images'])


