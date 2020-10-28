a=0
b=0
countera=0
counterb=0
finalanswer=0
while a<101:
    countera=a**2 + countera
    a+=1
while b<101:
    counterb=counterb+b
    b+=1
finalanswer = counterb**2 - countera
print(finalanswer)