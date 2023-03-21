# import itertools
import requests

로그인패킷 = {
    'id' : 'seona',
    'pw' : '1234',
}


address = requests.post('http://127.0.0.1:8080/', data=로그인패킷)
    
'''
문자열 = '0123456789'

"""
for i in 문자열:
    for j in 문자열:
        print(i, j);

for i in 문자열:
    for j in 문자열:
        for k in 문자열:
            print(i, j, k);
"""

for 패스워드길이 in range(1, 5):
    for password in itertools.product(문자열, repeat=패스워드길이):
        print(password)
        print(''.join(password))
'''

