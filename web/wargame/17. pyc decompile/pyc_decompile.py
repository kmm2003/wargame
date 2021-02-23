import time
from sys import exit
from hashlib import sha512

def GIVE_ME_FLAG(flag):
    if flag[:43] != 'http://wargame.kr:8080/pyc_decompile/?flag=':
        die()
    flag = flag[43:]
    now = time.localtime(time.time())
    print(now)
    seed = time.strftime('%m/%d/HJEJSH', time.localtime())
    print(seed)
    hs = sha512(seed.encode('utf-8')).hexdigest()
    start = now.tm_hour % 3 + 1
    end = start * ((now.tm_min+3) % 30 + 10)
    ok = hs[start:end]
    print(ok)
    
if __name__ == '__main__':
    GIVE_ME_FLAG('http://wargame.kr:8080/pyc_decompile/?flag=')