from requests import get
encrypted_cookie = get("https://aes.cryptohack.org/flipping_cookie/get_cookie/").json()["cookie"]
cipher, iv, fake = encrypted_cookie[32:], list(bytes.fromhex(encrypted_cookie[:32])), list(bytes.fromhex("5a05090407537b351e06"))
for i in range(len(fake)): iv[i] ^= fake[i]
print(get(f"https://aes.cryptohack.org/flipping_cookie/check_admin/{cipher}/{''.join([hex(i)[2:].zfill(2) for i in iv])}").json()["flag"])