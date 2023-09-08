#!/usr/bin/env python3
from Crypto.Util.number import inverse

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





G = (1804,5368)
Q_A = (815, 3190)
n_B = 1829

from hashlib import sha1
print("crypto{" + f'{sha1(str(scalar_multiplication(n_B, Q_A)[0]).encode()).hexdigest()}'+"}")
