p = 857504083339712752489993810777
e = 65537
q = 1029224947942998075080348647219

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


print(modinv(e, (p - 1) * (q - 1)))
#from math import gcd

#phi = (p-1)*(q-1)
#for i in range(2**15, 2**30):
#	if i*e % phi == 1:
#		print(i)
#		break
