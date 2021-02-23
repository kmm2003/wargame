import hashlib
import random
for i in range(10000000,30000000):
    hash1=str(i)+'salt_for_you'
    hash2=hash1.encode()
    for j in range(500):
        hash3=hashlib.sha1(hash2).hexdigest()
    f=open('table.txt','a')
    data=hash1+':  '+hash3
    f.write(data)
f.close()