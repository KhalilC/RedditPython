# Retrieves quotes and links from 'today i learned' and prints them out

import requests
import json
import time


while True:
    r = requests.get(r'http://www.reddit.com/r/todayilearned/new/.json')
    data = r.json() 
    for fact in data['data']['children']:
        print(fact['data']['title'][4:].capitalize())
        print(fact['data']['url'])
        print()
    time.sleep(35)