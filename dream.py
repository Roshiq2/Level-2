class roshiq:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __add__(self,other):
        x=self.name+other.name
        y=self.age+other.age
        return roshiq(x,y)
        

fo=roshiq(1,2)
ro=roshiq(2,3)
x=fo+ro
print(x.age)
