class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
obj1=rectangle(5,6)
obj2=rectangle(3,4)
areaone=obj1.area()
areatwo=obj2.area()
perimeterone=obj1.perimeter()
perimetertwo=obj2.perimeter()
print("first area and perimeter is",areaone,perimeterone)
print("second area and perimeter is",areatwo,perimetertwo)
if areaone>areatwo:
    print("areaone is larger")
elif arreaone<areatwo:
    print("areatwo is larger")
else:
    print("both  areas are equal")
    
