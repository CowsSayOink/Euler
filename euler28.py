import numpy as np
import sympy
a=1
total=0
gap=1
timer=1
prime=0
while a<35 or(prime*100)/(total)>=10:
    if timer==5:
        gap+=2
        timer=1
    total+=1
    if sympy.isprime(a):
        prime+=1
    a+=gap+1
    timer+=1
    
print(prime/total,np.sqrt(a))











































