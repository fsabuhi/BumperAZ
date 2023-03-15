
from main import get_cars
import json
import requests

def send_media_group(bot_id,chat_id,mediagroup):
    print(requests.post('https://api.telegram.org/bot{}/sendMediaGroup'.format('5686031636:AAGlVULyOcEhn3b9l1CUstZbUZFhfTvCbK0'),data={'chat_id': chat_id, 'media': json.dumps(mediagroup)}))
botid = '5686031636:AAGlVULyOcEhn3b9l1CUstZbUZFhfTvCbK0'
def auto_send(db) -> None: #,autos:list,user:str
    for i in db['users'].keys():
        user_id = i
        for i in db['users'][i]:
            data = get_cars(i)
            for i in range(data.ads_count):
                images = [dict(type='photo',media= i) for i in data.images[i]]
                images[0]['caption'] = data.car[i]
                send_media_group(bot_id=botid,chat_id=user_id,mediagroup=images)

db = json.load(open('registered_users.json','r'))

print(auto_send(db))
 