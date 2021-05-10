




def sol(p):
    total=0
    for i in range(p-1,2,-1):
        n=(p-2*(i**2))//(2*i)
        if 2*(i**2)+2*i*n==p and i>n and n>0:
           total+=1
    return total
print(sol(120))












































