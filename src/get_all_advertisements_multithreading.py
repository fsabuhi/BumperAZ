from turbo_az import get_advertisement_info
import time
from random import randint
import json
import threading
from random import choice
from random import getrandbits
def get_sent_request() -> list:
    with open("src/sent_requests_id.txt", "r") as fp:
        sent_requests_id = []
        for i in fp:
            x = i[:-1]
            sent_requests_id.append(x)
        fp.close()
        return sent_requests_id

def create_new_file_and_add_data(new_data:dict):
    filename = getrandbits(128)
    with open(f"data/{filename}.json", "w") as outfile:
        json.dump(new_data, outfile,indent = 4)
        outfile.close()  
        
def update_data(new_data:dict):
    with open("src/data.json", "r" ) as outfile:
        db = json.loads(outfile.read())
        db.update(new_data)
        outfile.close()
    with open("src/data.json", "w" ) as outfile:
        json.dump(db, outfile,indent = 4)
        outfile.close()

def update_sent_request(new_ids:list):
    with open("src/sent_requests_id.txt", "a") as fp:
        for _id in new_ids:
            fp.write("{}\n".format(_id)) 
        fp.close()

def get_data(id,proxy):
    url = "http://turbo.az/autos/{}".format(id)
    data = get_advertisement_info(url,proxy)
    return data

def main(count):
    proxies = [{
    "http": "socks5://csjgoxeo:27vihucfp3ql@2.56.119.93:5074/",
    "https": "socks5://csjgoxeo:27vihucfp3ql@2.56.119.93:5074/"
},
{
    "http": "socks5://csjgoxeo:27vihucfp3ql@45.94.47.66:8110/",
    "https": "socks5://csjgoxeo:27vihucfp3ql@45.94.47.66:8110/"
},{
    "http": "socks5://csjgoxeo:27vihucfp3ql@45.155.68.129:8133/",
    "https": "socks5://csjgoxeo:27vihucfp3ql@45.155.68.129:8133/"
},{
    "http": "socks5://csjgoxeo:27vihucfp3ql@154.95.36.199:6893/",
    "https": "socks5://csjgoxeo:27vihucfp3ql@154.95.36.199:6893/"
},{
    "http": "socks5://csjgoxeo:27vihucfp3ql@185.199.228.220:7300/",
    "https": "socks5://csjgoxeo:27vihucfp3ql@185.199.228.220:7300/"
},{
    "http": "socks5://csjgoxeo:27vihucfp3ql@185.199.229.156:7492/",
    "https": "socks5://csjgoxeo:27vihucfp3ql@185.199.229.156:7492/"
},{
    "http": "socks5://csjgoxeo:27vihucfp3ql@185.199.231.45:8382/",
    "https": "socks5://csjgoxeo:27vihucfp3ql@185.199.231.45:8382/"
},{
    "http": "socks5://csjgoxeo:27vihucfp3ql@188.74.183.10:8279/",
    "https": "socks5://csjgoxeo:27vihucfp3ql@188.74.183.10:8279/"
},{
    "http": "socks5://csjgoxeo:27vihucfp3ql@188.74.210.21:6100/",
     "https": "socks5://csjgoxeo:27vihucfp3ql@188.74.210.21:6100/"
}]
    
    proxies_new = [{
    "http": "http://csjgoxeo:27vihucfp3ql@2.56.119.93:5074/"
},
{
    "http": "http://csjgoxeo:27vihucfp3ql@45.94.47.66:8110/"
},{
    "http": "http://csjgoxeo:27vihucfp3ql@45.155.68.129:8133/"
},{
    "http": "http://csjgoxeo:27vihucfp3ql@154.95.36.199:6893/"
},{
    "http": "http://csjgoxeo:27vihucfp3ql@185.199.228.220:7300/"
},{
    "http": "http://csjgoxeo:27vihucfp3ql@185.199.229.156:7492/"
},{
    "http": "http://csjgoxeo:27vihucfp3ql@185.199.231.45:8382/"
},{
    "http": "http://csjgoxeo:27vihucfp3ql@188.74.183.10:8279/"
},{
    "http": "http://csjgoxeo:27vihucfp3ql@188.74.210.21:6100/"
}]
    
    proxy = choice(proxies)
    start_time = time.time()
    data = {}
    old_sent_requests = get_sent_request()
    sent_requests = []
    for i in range(count):
        id = randint(1000000,9999999)
        if id not in sent_requests:
            try:
                data.update({id : get_data(id,proxy)})
            except:
                pass
        sent_requests.append(id)
    
    update_sent_request(sent_requests)
    create_new_file_and_add_data(data)
    #update_data(data)
    print((time.time()-start_time)/count)

        

if __name__ == '__main__':
    while True:
        threads = []
        thread_count = 100
        for i in range(thread_count):
            t = threading.Thread(target=main,args=[10])
            t.daemon=True
            threads.append(t)
        for i in range(thread_count):
            threads[i].start()
        for i in range(thread_count):
            threads[i].join()



