s='12'

def pad(p,up):
    if len(up)==0:
        print(p)
        return
    digit=int(up[0])

    for i in range((digit-1)*3,digit*3):
        pad(p+chr(i+97),up[1:])


pad('',s)