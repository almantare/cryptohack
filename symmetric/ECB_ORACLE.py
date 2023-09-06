import requests
from string import printable

encrypt = lambda plaintext: requests.get('https://aes.cryptohack.org/ecb_oracle/encrypt/' + plaintext + '/').json()['ciphertext']
print_blocks = lambda x: [print(x[32 * i:32 + i * 32]) for i in range(0, len(x) // 32)]
plaintext = ""
first_block_found, second_block_found = len(plaintext), 0


while "}" not in plaintext:
    for ch in printable:
        if first_block_found < 16:
            payload = "00" * (16 - len(plaintext.encode('ascii').hex()) // 2 - 1) + plaintext.encode('ascii').hex() + ch.encode('ascii').hex() + "00" * (16 - len(plaintext.encode('ascii').hex()) // 2 - 1)
            ciphertext = encrypt(payload)
            print(payload, ch)
            if ciphertext[:32] == ciphertext[32:64]:
                plaintext += ch
                first_block_found += 1
                print(plaintext)
                break
        else:
            payload = plaintext.encode('ascii').hex()[2 + 2 * second_block_found:] + ch.encode('ascii').hex() + "00" * (16 - second_block_found - 1)
            ciphertext = encrypt(payload)
            print(payload, ch)
            if ciphertext[:32] == ciphertext[64:96]:
                plaintext += ch
                second_block_found += 1
                print(plaintext)
                break

