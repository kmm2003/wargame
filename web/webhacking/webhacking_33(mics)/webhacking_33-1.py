''' 
2단계
from requests import *
url='https://webhacking.kr/challenge/bonus-6/lv2.php'
cookies={'PHPSESSID':'2muaaqhhsat8jjhff57qqp1d1e'}
data={'post':'hehe','post2':'hehe2'}
response=post(url=url,cookies=cookies,data=data)
print(response.text)
'''

'''
4단계
from requests import *
from hashlib import *
url='https://webhacking.kr/challenge/bonus-6/l4.php'
cookies={'PHPSESSID':'2muaaqhhsat8jjhff57qqp1d1e'}
key=':'
response=get(url=url,cookies=cookies)
t=response.text
index=t.find(key)
time=t[index+2:index+12]
print(time)
encoded_string = time.encode()
hexdigest = md5(encoded_string).hexdigest()
url=f'https://webhacking.kr/challenge/bonus-6/l4.php?password={hexdigest}'
response=get(url=url,cookies=cookies)
print(response.text)
'''

'''
5단계
from requests import *
url='https://webhacking.kr/challenge/bonus-6/md555.php?imget=123'
cookies={'PHPSESSID':'2muaaqhhsat8jjhff57qqp1d1e','imcookie':'123'}
data={'impost':'123'}
response=post(url=url,cookies=cookies,data=data)
print(response.text)
'''

'''
6단계
from requests import *
from hashlib import *
url='https://webhacking.kr/challenge/bonus-6/gpcc.php'
cookies={'PHPSESSID':'2muaaqhhsat8jjhff57qqp1d1e'}
response=get(url=url,cookies=cookies)
t=response.text
agent='python-requests/2.23.0'
ip='211.106.76.247'
print(agent)
print(ip)
encoded_string = agent.encode()
hexdigest_agent = md5(encoded_string).hexdigest()
encoded_string_ip = ip.encode()
hexdigest_ip = md5(encoded_string_ip).hexdigest()
cookies={'PHPSESSID':'2muaaqhhsat8jjhff57qqp1d1e','test':hexdigest_ip}
data={'kk':hexdigest_agent}
response=post(url=url,cookies=cookies,data=data)
print(response.text)
'''

'''
8단계
from requests import *
url='https://webhacking.kr/challenge/bonus-6/wtff.php?21110676247=21110676247'
cookies={'PHPSESSID':'2muaaqhhsat8jjhff57qqp1d1e'}
response=get(url=url,cookies=cookies)
print(response.text)
'''
'''
9단계
from requests import *
answer=''
for i in range(97,122,2):
    answer+=chr(i)
    
url=f'https://webhacking.kr/challenge/bonus-6/nextt.php?ans={answer}'
cookies={'PHPSESSID':'2muaaqhhsat8jjhff57qqp1d1e'}
response=get(url=url,cookies=cookies)
print(response.text)
'''