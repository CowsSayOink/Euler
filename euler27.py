import sympy 
import numpy as np

def primes(p):
    n=0
    primeset=[2]
    candidate=3
    while primeset[-1]<p:
        if candidate%primeset[n]==0:
            n=0
            candidate+=2
            continue
        elif primeset[n]>np.sqrt(candidate):
            primeset.append(candidate)
            n=0
            candidate+=2
            continue
        else:
            n+=1
    return primeset


def polynomial(b,c):
    x=0
    count=0
    while True:
        if sympy.isprime(x**2+b*x+c):
            count+=1
            x+=1
        else:
            return count


print(polynomial(-79, 1601))


dictionary={}
for c in primes(997)[13:]:
    for b in range(-999,1000,2):
        a=[b,c]
        dictionary[str(a)]=polynomial(b, c)
p=list(dictionary.values())
o=list(dictionary.keys())
print(o[p.index(max(p))])




























