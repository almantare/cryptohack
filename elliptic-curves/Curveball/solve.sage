p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff

a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc

b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b

F = GF(p)

E = EllipticCurve(F, [a, b])


# Public key of www.bing.com

public = E(0x3B827FF5E8EA151E6E51F8D0ABF08D90F571914A595891F9998A5BD49DFA3531, 0xAB61705C502CA0F7AA127DEC096B2BBDC9BD3B4281808B3740C320810888592A)


# Order of the group a

# a = 115792089210356248762697446949407573529996955224135760342422259061068512044369

a = E.order()
print(a)
print(public * (a + 1) == public)
from pwn import *
conn = remote('socket.cryptohack.org', 13382)
print(conn.readline())
