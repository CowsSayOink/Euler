

a='''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

a=a.split('\n')
a.remove('')
a.remove('')
print(a)

aa=[]
for x in range(len(a)):
    c=[]
    b=a[x].split()
    for y in range(len(b)):
        c.append(int(b[y]))
    aa.append(c)
print(aa)

total=[]


for c in range(2):
    for d in range(2):
        for e in range(2):
            for f in range(2):
                for g in range(2):
                    for h in range(2):
                        for i in range(2):
                            for j in range(2):
                                for k in range(2):
                                    for l in range(2):
                                        for m in range(2):
                                            for n in range(2):
                                                for o in range(2):
                                                    for p in range(2):
                                                        position=c
                                                        subtotalc=aa[1][position]
                                                        position+=d
                                                        subtotald=aa[2][position]
                                                        position+=e
                                                        subtotale=aa[3][position]
                                                        position+=f
                                                        subtotalf=aa[4][position]
                                                        position+=g
                                                        subtotalg=aa[5][position]
                                                        position+=h
                                                        subtotalh=aa[6][position]
                                                        position+=i
                                                        subtotali=aa[7][position]
                                                        position+=j
                                                        subtotalj=aa[8][position]
                                                        position+=k
                                                        subtotalk=aa[9][position]
                                                        position+=l
                                                        subtotall=aa[10][position]
                                                        position+=m
                                                        subtotalm=aa[11][position]
                                                        position+=n
                                                        subtotaln=aa[12][position]
                                                        position+=o
                                                        subtotalo=aa[13][position]
                                                        position+=p
                                                        subtotalp=aa[14][position]
                                                        
                                                        total.append(subtotalc+subtotald+subtotale+subtotalf+subtotalg+subtotalh+subtotali+subtotalj+subtotalk+subtotall+subtotalm+subtotaln+subtotalo+subtotalp+aa[0][0])

    







print(max(total))
















