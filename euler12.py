

def sum(a):
    return a*(a+1)//2







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



#take the elements one by one and divide them over and over and count how many there are. then with a given prime number look at 





def divisors(a):
    t=1
    c=0
    if a%2==1:
        while t<a//2+1:
            if a%t==0:
                c+=1
            t+=2
        return c+1
    else:
        while t<a//2+1:
            if a%t==0:
                c+=1
            t+=1
        return c+1
p=1
tracker=1
while divisors(p)<500:
    
    tracker+=1
    p+=tracker
    
print(p)










ways=0
for a in range (0,2):
    for b in range (0,3):
        for c in range (0,5):
            for d in range (0,11):
                for e in range (0,21):
                    for f in range (0,41):
                        for g in range (0,101):
                            for h in range (0,201):
                                if 200*a+100*b+50*c+20*d+10*e+5*f+2*g+h==200:
                                    ways+=1
print(ways)

























