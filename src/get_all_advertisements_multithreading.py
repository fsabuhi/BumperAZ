from turbo_az import get_advertisement_info
import time
from random import randint
import json
import threading

def get_sent_request() -> list:
    with open("src/sent_requests_id.txt", "r") as fp:
        sent_requests_id = []
        for i in fp:
            x = i[:-1]
            sent_requests_id.append(x)
        fp.close()
        return sent_requests_id

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

def get_data(id):
    url = "https://turbo.az/autos/{}".format(id)
    data = get_advertisement_info(url)
    return data

def main(count):
    start_time = time.time()
    data = {}
    old_sent_requests = get_sent_request()
    sent_requests = []
    for i in range(count):
        id = randint(1000000,9999999)
        if id not in sent_requests:
            try:
                data.update({id : get_data(id)})
            except:
                pass
        sent_requests.append(id)
    update_sent_request(sent_requests)
    update_data(data)
    print((time.time()-start_time)/count)

        

if __name__ == '__main__':
    threads = []
    thread_count = 25

    for i in range(thread_count):
        t = threading.Thread(target=main,args=[25])
        t.daemon=True
        threads.append(t)

    for i in range(thread_count):
        threads[i].start()
        time.sleep(1)
    for i in range(thread_count):
        threads[i].join()



