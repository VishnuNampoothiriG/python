class time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):
        return self.__hour+other.__hour,self.__minute+other.__minute,self.__second+other.__second
obj1=time(2,30,10)
obj2=time(1,30,40)
print("time is :",obj1+obj2)
