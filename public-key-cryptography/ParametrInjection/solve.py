#!/bin/python3 
from pwn import *
from json import loads, dumps
from decrypt import decrypt_flag
import hashlib
from Crypto.Cipher import AES

conn = remote('socket.cryptohack.org', 13371)
captured = loads(str(conn.recvline()).encode('ascii')[26:-3])
#print(captured)
p = captured["p"]
g = captured["g"]
A = captured["A"]

payload = dumps({"p": p, "g": g, "A": p})
#print(f"{payload=}")
#print(p, g, A)
conn.sendlineafter(": ", payload)
conn.readuntil(": ")
line = loads(conn.readline().strip().decode())
B = int(line['B'], 16)
payload = dumps({"B": p})
print(payload, len(payload))
conn.sendlineafter(": ", payload)
conn.readuntil(": ")
line = loads(conn.readline().strip().decode())
iv = bytes.fromhex(line['iv'])
encrypted_flag = bytes.fromhex(line['encrypted_flag'])
sha1 = hashlib.sha1()
secret = 0
sha1.update(str(secret).encode())
key = sha1.digest()[:16]
aes = AES.new(key, AES.MODE_CBC, iv)
print(aes.decrypt(encrypted_flag))
