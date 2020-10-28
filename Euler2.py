x=1
y=1
z=0
t=0
while x<4000000:
    z=x+y
    x=y+z
    y=x+z
    if x%2==0: 
        t=t+x
    if y%2==0: 
        t=t+y
    if z%2==0: 
        t=t+z



print("x is", x)
print("y is", y)
print("z is", z)
print(t)



