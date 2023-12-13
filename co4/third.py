class rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def area(self):
        return self.__length*self.__breadth
    def __lt__(self,other):
        return self.area<other.area
obj1=rectangle(6,4)
obj2=rectangle(4,5)
area1=obj1.area()
area2=obj2.area()
if(area1<area2):
    print(area2,"(area2) is larger")
else:
    print(area1,"(area1) is larger")
