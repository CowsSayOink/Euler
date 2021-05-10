def sumdigits(n): 
    total=0
    for a in str(n):
        total+=int(a)
    return total

class fraction:
    def __init__(self, num,den):
        self.num=num
        self.den=den
    def __add__(self,other):
        top=self.num*other.den+other.num*self.den
        bottom=self.den*other.den
        a=fraction(top,bottom)
        """
        simplifies it
        for b in range(1+bottom//2,2,-1):
            if bottom%b==0 and top%b==0:
                c=fraction(top//b, bottom//b)
                return c
        """
        return a
    
    
    def simplify(self):
        """ does not work"""
        top=self.num
        bottom=self.den
        for b in range(1+bottom//2,2,-1):
            if bottom%b==0 and top%b==0:
                c=fraction(top//b, bottom//b)
                return c
            else:
                return self
            
    def flip(self):
        a=self.num
        b=self.den
        new=fraction(b, a)
        return new
        
    def __repr__(self):
        return str([self.num,self.den])

def number(n):
    if n%3==0:
        return 2*n//3
    else:
        return 1
    

"""
a=fraction(4, 8)
b=fraction(8, 9)
print(a+b,(a+b).flip(),(a+b).simplify())
"""

n=100
first=fraction(1, number(n)) 
while n>2:
    
    second=fraction(number(n-1),1)
    third=(first+second).flip()
    n-=1
    first=third
final=(fraction(2, 1)+third)
print(sumdigits(final.num))
































