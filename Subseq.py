def sub(p,up,li):
    if len(up)==0:
        li.add(p)
        return
    ch=up[0]
    sub(p+ch,up[1:],li)
    sub(p,up[1:],li)
    return li

print(sub("","abcd",set([])))

