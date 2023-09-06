p = 991
g = 209
for d in range(100000000):
	if d * g % p == 1:
		print(d)
		break
