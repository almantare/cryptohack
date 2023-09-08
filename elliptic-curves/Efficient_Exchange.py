#!/usr/bin/env python3
from Crypto.Util.number import inverse
from Decrypt import decrypt_flag
from hashlib import sha1

#what the heck is this task?
a = 497
b = 1768
p = 9739


def point_addition(P, Q):
	# Define zero
	O = (0, 0)
	# If P = O, then P + Q = Q
	if P == O:
		return Q
    	# If Q = O, then P + Q = P
	if Q == O:
		return P

	# Otherwise, write P = (x1, y1) and Q = (x2, y2)
	x1, y1 = P[0], P[1]
	x2, y2 = Q[0], Q[1]

	# If x1 = x2 and y1 = -y2, then P + Q = O
	if x1 == x2 and y1 == -y2:
		return O

	# Otherwise, if P ≠ Q: λ = (y2 - y1) / (x2 - x1)
	if P != Q:
		lam = ((y2 - y1) * inverse(x2 - x1, p)) % p

	# If P = Q: λ = (3 * x1**2 + a) / 2 * y1
	else:
		lam = ((3 * x1**2 + a) * inverse(2 * y1, p)) % p

	# x3 = λ**2 - x1 - x2, y3 = λ * (x1 - x3) - y1
	x3 = (lam**2 - x1 - x2) % p
	y3 = (lam * (x1 - x3) - y1) % p
	# P + Q = (x3, y3)
	summation = (x3, y3)

	return summation


def scalar_multiplication(n, P):
	# Define zero
	O = (0, 0)
	# Set Q = P and R = O
	Q, R = P, O

	while n > 0:
		# If n ≡ 1 mod 2, set R = R + Q
		if n % 2 == 1:
			R = point_addition(R, Q)
		# Set Q = 2Q and n = ⌊n/2⌋
		Q = point_addition(Q, Q)
		n //=2
	return R

def sqrt(x, p):
    for i in range(1, p):
        if pow(i, 2) % p == x:
            return (i, p - i)
    return None


G = (1804,5368)
q_x = 4726
n_B = 6534
creds = {'iv': 'cd9da9f1c60925922377ea952afc212c', 'encrypted_flag': 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'}
y1, y2 = sqrt((pow(q_x, 3) + a * q_x + b) % p, p)
Q1, Q2 = (q_x, int(y1)), (q_x, int(y2))
if Q1[1] % 4 == 3:
	secret = scalar_multiplication(Q1, n_B)
	print(decrypt_flag(scalar_multiplication(n_B, Q1)[0], creds["iv"], creds["encrypted_flag"]))
else:
	print(decrypt_flag(scalar_multiplication(n_B, Q2)[0], creds["iv"], creds["encrypted_flag"]))
