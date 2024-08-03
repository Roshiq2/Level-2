def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    
def convert(ros):
    i=0
    sum=0
    while i < len(ros):
        s1=value(ros[i])
        if i == len(ros)-1:
            sum+=s1
            i+=1
        else:
            s2=value(ros[i+1])
            if s2 > s1:
                sum+=s2-s1
                i+=2
            else:
                sum+=s1
                i+=1
    return sum

print(convert("III"))