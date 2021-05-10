def factorial(n):
    if n<=0:
        return 1
    else:
        return n*factorial(n-1)

facset=[]
for a in range(1,10):
    print(a,factorial(a))
    facset.append(factorial(a))
facset.reverse()
print(facset)

n=999999
nset=[]
for a in facset:
    nset.append(n//a)
    n=n-(n//a)*a
print(nset)

numbers=[0,1,2,3,4,5,6,7,8,9]
finalanswer=[]
for a in nset:
    finalanswer.append(numbers[a])
    numbers.remove(numbers[a])
finalanswer.append(numbers)
print(finalanswer)
















