a='cghe'
b='xhy'
m,n=len(a),len(b)
li=[[0]*(n+1) for i in range(m+1)]
for i in range(1,m+1): #1234
    for j in range(1,n+1): #123
        if(a[i-1]==b[j-1]):
            li[i][j]=1+(li[i-1][j-1])
        else:
            li[i][j]=max(li[i][j-1],li[i-1][j])
print(li[-1][-1])