from collections import defaultdict
s='abcdefghi'
li= defaultdict(int)
for i in s:
    li[i]+=1
print(li.keys())
se=set(li.values())

print(se)
print(len(se))
if len(se)==1:
    print('True')
elif len(se)==2:
    print("roshiq")
    if list(se)[0]-1==list(se)[1] or list(se)[0]-1==0 :
        print('True')
    else:
        print('False')
else:
    print('False')