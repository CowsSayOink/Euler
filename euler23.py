

def sumdivisors(n):
    j=[1]
    for i in range(2,1+ n//2):
        if n%i==0:
            j.append(i)
    return sum(j)

abundant=[]
for i in range(12,28124):
    if sumdivisors(i)>i:
        abundant.append(i)

sumset={5}
for a in abundant:
    for b in abundant:
        if a+b>28123:
            continue
        else:
            sumset.add(a+b)


sumset.remove(5)
bigmax=28123*28124//2
print(bigmax-sum(sumset))






















