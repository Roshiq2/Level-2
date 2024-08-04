s='abcd'

for i in range(len(s)):
    x=s[i]

    print(x, end=' ')
    for j in range(i+1,len(s)):
        y=s[i]+s[j]
        x+=s[j]
        print(y, end=' ')
        if x!=y: print(x, end=' ')
