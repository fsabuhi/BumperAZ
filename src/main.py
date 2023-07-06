class get_cars:
    def __init__(self,model):
        from get_advertisement_info import get_advertisement_info as info
        from get_advertisement_links import get_advertisement_links as ads
        from link_generator import link_generator as link
        from id_generator import id_generator as id
        car = id(model)
        brand_id = car.brand_id
        model_id = car.model_id

        link = link(model_id).link

        ads_links = ads(link).urls
        
        self.car=[]
        self.images=[]
        self.ads_count=len(ads_links)
        for i in ads_links:
            data = info(i)
            self.car.append('{}\n{}\n{}'.format(data.car_details,data.car_price,i))
            self.images.append(data.images)


