import numpy as np

from functions import primeset

"""
def sum_digit(n):
    t=0
    while n>0:
        t+=n%10
        n//=10
    return t

the_big_set=[]

for a in range(1,100):
    for b in range(1,100):
        the_big_set.append(sum_digit(a**b))
print(max(the_big_set))



n=0
primeset=[2]
t=2
candidate=3
counter=1
while len(primeset)<100:
    if candidate%primeset[n]==0:
        n=0
        candidate+=2
        continue
    elif primeset[n]>np.sqrt(candidate):
        primeset.append(candidate)
        n=0
        print(candidate)
        candidate+=2
        continue
    else:
        n+=1

print(primeset)


counter=0
for a in range(1,100):
    for b in range(1,100):
        if len(str(a**b))==b:
            counter+=1
            
print(counter)

"""



solutionset=[]

def totient(n):
    a=0
    b=[]
    while primeset[a]<np.sqrt(n):
        if n%primeset[a]==0:
            b.append(primeset[a])
            a+=1
        else:
            a+=1
    for c in range(0,len(b)):
        n*=((b[c]-1)/b[c])
    return n

for a in range(5,1000000):
    solutionset.append(a/totient(a))
print(solutionset.index(max(solutionset)))



































