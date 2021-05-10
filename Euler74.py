def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

def facchain(n):
    thelist=[]
    a=0
    condition=True
    while condition and len(thelist)<62:
        for i in str(n):
            a+=factorial(int(i))
        if a in thelist:
            condition=False
        thelist.append(a)
        n=a
        a=0
        
    return len(thelist)
answer=0
for i in range(1000000):
    if facchain(i)==60:
        answer+=1
        

print(answer)


