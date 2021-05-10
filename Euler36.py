def conv(x):
    """ Converts from binary to decimal"""
    return int(x[2:])


def ispal(x):
    a=str(x)
    b=len(a)
    for c in range((b//2)+1):
            if a[c]!=a[-1-c]:
                return False
    return True

total=0

for a in range(1000000):
    if ispal(a)and ispal(conv(bin(a))):
        total+=a
print(total)



























