boo=[[True,True,True] for x in range(3)]

def path(p, r, c, boo):
    if r==len(boo)-1 and c==len(boo[0])-1:
        print(p)
        return
    if boo[r][c]!=True:
        return

    # boo[r][c]=False
    if r<len(boo)-1:
        path(p +'R', r + 1, c, boo)
    if c<len(boo)-1:
        path(p +'D', r, c + 1, boo)
    # if r>0:
    #     path(p + 'U', r - 1, c, boo)
    # if c>0:
    #     path(p + 'L', r, c - 1, boo)
    # boo[r][c]=True


path('',0,0,boo)