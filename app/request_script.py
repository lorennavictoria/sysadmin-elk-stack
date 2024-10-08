import requests
import random
import time

url = 'http://localhost:8888'

while True:
    sleep_time = random.randint(1, 5)
    request_num = random.randint(1, 30)
    
    print(f'Sending {request_num} requests to server. Sleeping {sleep_time} seconds')
    
    for i in range(request_num):
        requests.get(f'{url}/simulate?type=ERROR')
        
    time.sleep(sleep_time)
