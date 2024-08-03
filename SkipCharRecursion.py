s='bccaacdac love'
def fun(e,s):
    if len(s)==0:
        print(e)
        return
    a=s[0]
    if a=='a':
        fun(e,s[1:])
    else:
        fun(e+a,s[1:])

# fun('',s)

print(s.split(' '))

