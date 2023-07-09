from turbo_az import get_advertisement_info
import time
from random import randint
import json
import threading
time_data = []
while True:
    start_time = time.time()
    with open('data.json',"r") as json_file:
        db = json.load(json_file)

    with open("sent_requests_id.txt", "r") as fp:
        sent_requests_id = []
        for i in fp:
            x = i[:-1]
            sent_requests_id.append(x)
        #sent_requests_id.append(list(db.keys()))
    request_count = 10
    def get_data():
        for j in range(request_count):
            i = randint(1000000,10000000)
            if i not in sent_requests_id:  #randomize sent requests. it is slower but less obvious
                start_time = time.time()
                try:
                    url = 'https://turbo.az/autos/{}'.format(i)
                    print(url)
                    data = get_advertisement_info(url)
                    db[i]=data
                    sent_requests_id.append(i)
                except IndexError:
                    pass
    def save():
        with open("sent_requests_id.txt", "w") as fp:
            for _id in sent_requests_id:
                fp.write("{}\n".format(_id))
        fp.close()
        with open("data.json", "w") as outfile:
            json.dump(db, outfile)
        outfile.close()
    threads=[]
    thread_count = 10
    for i in range(thread_count):
        t = threading.Thread(target=get_data)
        t.daemon=True
        threads.append(t)
    for i in range(thread_count):
        threads[i].start()
    for i in range(thread_count):
        threads[i].join()
    save()
    time_spent = time.time()-start_time
    time_data.append(time_spent)
    avg = sum(time_data)/len(time_data)
    print('time left:',((10000000-len(sent_requests_id))/(thread_count*request_count))*avg/60/60,'HOURS')
    sent_requests_id.append(i)
    print('DONE!!!')






