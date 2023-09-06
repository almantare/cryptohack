from requests import get
encrypted_flag = get("https://aes.cryptohack.org/symmetry/encrypt_flag/").json()["ciphertext"]
print(encrypted_flag)
decrypt_block = lambda block, iv: get(f"https://aes.cryptohack.org/symmetry/encrypt/{block}/{iv}").json()["ciphertext"]
from pwn import xor
print_block = lambda x: [print(x[i*32:i*32+32]) for i in range(len(x) // 32)]

print(encrypted_flag[64:])
print(xor(decrypt_block(encrypted_flag[32:64], encrypted_flag[:32]), encrypted_flag[64:]))
print()
print_block(encrypted_flag)
# crypto{0fb_15_5ymm37r1c4l_!!!11!}