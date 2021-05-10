pentagonal=[]

for a in range(1,150000):
    pentagonal.append((a*(3*a-1))//2)

duplicates=[]
minimums=[]
for a in pentagonal:
    for b in pentagonal:
        if a==b:
            continue
        elif abs(a-b) in pentagonal and a+b in pentagonal:
            minimums.append(abs(a-b))
            break
        '''    
for a,b in enumerate(pentagonal):
    for c,d in enumerate(pentagonal):
        if a==c:
            continue
        elif abs(d-b) in pentagonal and d+b in pentagonal:
            minimums.append(abs(a-b))
          '''  
            
            
            
            
            
            
print(min(minimums))











































