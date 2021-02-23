import base64
 
iv_encoded = '6l0s6EdDnRg='
data_encoded = 'lt6pchn0ZWQ='
 
iv = base64.b64decode(iv_encoded)
data = base64.b64decode(data_encoded)
 
guest = b'guest\x03\x03\x03' #추측한 guest 평문 값
admin = b'admin\x03\x03\x03' #추측한 admin 평문 값
 
middle = [ iv[i] ^ guest[i] for i in range(8) ] # guest 평문 + iv 생성 
changed_iv = [ middle[i] ^ admin[i] for i in range(8) ] # guest 평문 + iv + admin 평문 생성
print(base64.b64encode(bytes(changed_iv))) 
# changed_iv 에 저장된 (guest 평문 + iv + admin 평문) 리스트 값을 bytes값으로 하나로 변환 후 base64 인코딩하고 출력
