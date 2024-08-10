from itertools import zip_longest

v1='1.0'
v2='1.0.0.0'

def fu(v1,v2):
    i=0
    while i<len(v1) or i<len(v2):
        a=v1[i] if i<len(v1) else 0
        b=v2[i] if i<len(v2) else 0
        i+=1
        if a==b:
                continue
        return 1 if v1<v2 else -1

    else:
            return 0



def fun(v1,v2):
    for i,j in zip_longest(v1,v2,fillvalue=0):
        if i==j:
            continue
        return 1 if v1<v2 else -1
    else:
        return 0

v1=list(map(int,v1.split('.')))
v2=list(map(int,v2.split('.')))
print(v1, v2)
print(fun(v1,v2))

