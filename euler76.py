def factorial(n):
    if n<=0:
        return 1
    else:
        return n*factorial(n-1)


def chose(n,k):
    t=1
    for a in range(k+1,n+1):
        t*=a
    return t//(factorial(n-k))


total=0
for a in range(1,5):
    total+=chose(5-1,a)
    
    
    
print(total)






























