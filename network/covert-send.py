from pythonping import ping
from time import sleep

with open("#", "rb") as f:
    while True:
        byte = f.read(1024)
        if byte == b"": # EOF, NULL
            ping("#", verbose=True, count=1, payload=b"EOF")
            break
        ping("#", verbose=True, count=1, payload=byte)
        sleep(0.5)

