from Crypto.Cipher import AES
import hashlib
import random
from pwn import *
# conn = remote('aes.cryptohack.org/passwords_as_keys/encrypt_flag/', 80)
r = remote('aes.cryptohack.org/passwords_as_keys/encrypt_flag/', 81, level = 'debug')
# conn.recv()
# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words

FLAG =  "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


def brute(ciphertext):
    for word in open("words.txt", 'r'):
        word = word.replace("\n", "")

        word = hashlib.md5(word.encode()).hexdigest()
        # print(decrypt(FLAG, word))
        # print(word?)
        tmp = decrypt(FLAG, word)
        # print(bytes.fromhex(tmp['plaintext']))
        # print(bytes("crypto{", encoding="utf-8"))
        if bytes("crypto{", encoding='utf-8') in bytes.fromhex(tmp['plaintext']):
            print(word)
            print(bytes.fromhex(tmp['plaintext']))
            # print(tmp)

brute(FLAG)
