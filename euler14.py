
the_set=[]
numbers=[]

def collatz(n):
    steps=1
    while n>1:
        if n%2==0:
            n/=2
            steps+=1
        else:
            n=3*n+1
            steps+=1
    return steps
print(collatz(13))

for a in range(0,1000000):
    the_set.append(collatz(a))
    numbers.append(a)
    
p=max(the_set)

print(numbers[the_set.index(p)])







































