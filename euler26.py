

def cycle(k):
    n=1
    p=(k*10**n)-k
    while round(p,15)!=p:
        n+=1
        p=(k*10**n)-k
    return n
print(cycle(1/37))

l=[]
m=[]
for a in range(1,1000):
   l.append(a) 
   m.append(cycle(1/a))
print(l[m.index(max(m))])


































