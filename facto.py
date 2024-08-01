n=int(input())

ans=[]
def fun(s,r):
	li=[0]*256
	temp=''
	for i in s:
		if li[ord(i)]<r:
			temp+=i
			li[ord(i)]+=1
	ans.append(temp)

for i in range(n):	
	r=input().split(",")
	r=r[-1]
	s=input()
	fun(s,r)

for _ in ans:
	print(_)
