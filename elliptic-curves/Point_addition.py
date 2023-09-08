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

#--------Testing--------#


P = (493, 5564)
Q = (1539, 4742) 
R = (4403,5202)


S = point_addition(point_addition(point_addition(P, P), Q), R)
#print("crypto{%1, %2}" % S[0], S[1] )
#print('crypto{%(x), %(y)}' % {"x": str(S[0]), "y": str(S[1])})
print("crypto{"+ f"{S[0]}, {S[1]}" + "}")
