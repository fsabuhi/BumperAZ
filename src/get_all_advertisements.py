from turbo_az import get_advertisement_info
f = open("demofise2.txt", "a")
import time
from random import randint
time_data = []

# for i in range(1000000,10000000):
#     start_time = time.time()
#     try:
#         data = get_advertisement_info('https://turbo.az/autos/{}'.format(i))
#         f.write(data)
#     except IndexError:
#         print('x')
#     time_spent = time.time()-start_time
#     time_data.append(time_spent)
#     avg = sum(time_data)/len(time_data)
#     print('time left:',(10000000-i)*avg/60)
# f.close()

for i in range(50):
    i = randint(1000000,9999999)
    start_time = time.time()
    try:
        url = 'https://turbo.az/autos/{}'.format(i)
        data = get_advertisement_info(url)
        f.write(url)
        print(url,data['publish_date'])
    except IndexError:
        print('x')
    time_spent = time.time()-start_time
    time_data.append(time_spent)
    avg = sum(time_data)/len(time_data)
    print('time left:',(10000000-i)*avg/60) 
    time.sleep(5)
f.close()