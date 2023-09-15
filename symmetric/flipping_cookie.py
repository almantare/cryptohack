[print(__import__("requests").get("https://aes.cryptohack.org/flipping_cookie/check_admin/{cipher}/{iv}/".format(cipher=cipher, iv=''.join([hex(i)[2:].zfill(2) for i in [iv[i] ^ list(bytes.fromhex("".join(map(lambda x: hex(x)[2:].zfill(2), [[x for x in b";admin=Tru"][i] ^ [x for x in b"admin=Fals"][i] for i in range(10)]))))[i] if i in [x for x in range(len(list(bytes.fromhex("".join(map(lambda x: hex(x)[2:].zfill(2), [[x for x in b";admin=Tru"][i] ^ [x for x in b"admin=Fals"][i] for i in range(10)]))))))] else iv[i] for i in range(len(iv))]]))).json()["flag"]) for cipher, iv in list([[list(bytes.fromhex(x[0:32])) if i == 1 else x[32:] for i in range(2)] for x in [__import__("requests").get("https://aes.cryptohack.org/flipping_cookie/get_cookie/").json()["cookie"]]])]
"""
  _____           _   _                        ____    _   _            _       _ 
 |_   _|         | | (_)                      |  _ \  (_) | |          | |     | |
   | |    _ __   | |  _   _ __     ___        | |_) |  _  | |_    ___  | |__   | |
   | |   | '_ \  | | | | | '_ \   / _ \       |  _ <  | | | __|  / __| | '_ \  | |
  _| |_  | | | | | | | | | | | | |  __/  _    | |_) | | | | |_  | (__  | | | | |_|
 |_____| |_| |_| |_| |_| |_| |_|  \___| ( )   |____/  |_|  \__|  \___| |_| |_| (_)
                                        |/                                        
                                                                                  """

from requests import get
encrypted_cookie = get("https://aes.cryptohack.org/flipping_cookie/get_cookie/").json()["cookie"]
cipher, iv, fake = encrypted_cookie[32:], list(bytes.fromhex(encrypted_cookie[:32])), list(bytes.fromhex("5a05090407537b351e06"))
for i in range(len(fake)): iv[i] ^= fake[i]
print(get(f"https://aes.cryptohack.org/flipping_cookie/check_admin/{cipher}/{''.join([hex(i)[2:].zfill(2) for i in iv])}").json()["flag"])