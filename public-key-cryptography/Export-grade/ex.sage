K = GF(3^6,'b')

b = K.gen()

a = b^210

discrete_log(a, b, K.order()-1)
