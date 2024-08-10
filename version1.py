from itertools import zip_longest

v1=str(input())
v2=str(input())
v1= list(map(int, v1.split('.')))
v2=list(map(int, v2.split('.'))) 


for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
            if rev1 == rev2:
                    continue
            print("v1" if rev1>rev2 else "v2" )
    
       


