arr=[1,3,3,5,7]
t=5
def fu(arr,t,i=0,li=[]):
    if i==len(arr)-1:
        return li
    if arr[i]==t:
        li.append(i)
    return fu(arr,t,i+1,li)
        
    

print(fu(arr,t))



