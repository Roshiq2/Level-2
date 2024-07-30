i=0
n=[]

while len(n)!=77:
    if set(str(i)).issubset({'3','4'}):
        n.append(i)
    i+=1

print(n)