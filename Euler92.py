def cycle(p):

    while True:
        if p==89:
            return True
        elif p==1:
            return False
        else:
            b=0
            for a in str(p):
                b+=(int(a))**2
            p=b
            
tally=0
for a in range(1,10000000):
    if cycle(a):
        tally+=1
        
print(tally)
        
#This program can use some massive improvement by having a long list of all numbers up to ten million. When we run one loop we consider all the numbers in it and remove them from the list.










































