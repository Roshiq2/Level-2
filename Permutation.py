def per(p,up):
    if len(up)==0:
        print(p, end=' ')
        return

    ch=up[0]
    for i in range(len(p)+1):
        f=p[:i]
        s=p[i:]
        per(f+ch+s,up[1:])


per('','abc')