import requests
import random
import time

url = 'http://localhost:8888'


def simulate_request(url):
    requests.get(f'{url}/simulate')
    
    
def simulate_errors(url):
    rand = random.randint(1, 10)
    
    if rand > 8:
        requests.get(f'{url}/simulate')
    else:
        requests.get(f'{url}/simulate?type=ERROR')
        

while True:
    sleep_time = random.randint(1, 7)
    request_num = random.randint(1, 30)
    
    print(f'Sending {request_num} requests to server. Sleeping {sleep_time} seconds')
    
    for i in range(request_num):
        simulate_request(url)
        
    time.sleep(sleep_time)
