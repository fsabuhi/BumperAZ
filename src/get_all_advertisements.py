from turbo_az import get_advertisement_info
import time
from random import randint
import json
time_data = []
with open('/BumperAZ/src/data.json',"r") as json_file:
    db = json.load(json_file)

with open("/BumperAZ/src/sent_requests_id.txt", "r") as fp:
    sent_requests_id = []
    for i in fp:
        x = i[:-1]
        sent_requests_id.append(x)
    #sent_requests_id.append(list(db.keys()))

for j in range(9000000):
    i = randint(1000000,10000000)
    if i not in sent_requests_id:  #randomize sent requests. it is slower but less obvious
        start_time = time.time()
        try:
            data = get_advertisement_info('https://turbo.az/autos/{}'.format(i))
            db[i]=data
            with open("/BumperAZ/src/data.json", "w") as outfile:
                json.dump(db, outfile)
            outfile.close()
        except IndexError:
            pass
        time_spent = time.time()-start_time
        time_data.append(time_spent)
        print(time_data)
        avg = sum(time_data)/len(time_data)
        print('time left:',(10000000-j)*avg/60)
        sent_requests_id.append(i)
        with open("/BumperAZ/src/sent_requests_id.txt", "w") as fp:
            for _id in sent_requests_id:
                fp.write("{}\n".format(_id))