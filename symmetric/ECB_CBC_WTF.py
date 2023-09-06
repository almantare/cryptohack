import requests

ciphertext = requests.get("https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/").json()['ciphertext']

decode = lambda ciphertext: requests.get(f"https://aes.cryptohack.org/ecbcbcwtf/decrypt/{ciphertext}").json()['plaintext']

plaintext = ""

for i in range(32, 65, 32):
    intermediary = decode(ciphertext[i:i + 32])
    plaintext += hex(int(intermediary, 16) ^ int(ciphertext[i - 32:i], 16))[2:]

print(bytes.fromhex(plaintext))

