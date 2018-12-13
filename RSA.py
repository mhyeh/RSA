import math
import random

import prime
import util

def KeyGenerator(bit = 512):
    p = prime.PrimeGenerator(bit)
    q = prime.PrimeGenerator(bit)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 0
    d = 0
    while True:
        e = random.randrange(1, math.pow(2, 17))
        if math.gcd(phi_n, e) == 1:
            d = util.ModInv(e, phi_n)
            break
    return (n, p, q, e, d)
    
def Encryption(n, key, message):
    return util.SQandMU(message, key, n)

def DecryptionCRT(n, p, q, key, message):
    xp = message % p
    xq = message % q
    dp = key % (p - 1)
    dq = key % (q - 1)
    yp = util.SQandMU(xp, dp, p)
    yq = util.SQandMU(xq, dq, q)

    cp = util.ModInv(q, p)
    cq = util.ModInv(p, q)
    
    return (round(q * cp) * yp + round(p * cq) * yq) % n
