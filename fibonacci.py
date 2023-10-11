num=int(input("enter range:"))
f0=int(input("enter first number:"))
f1=int(input("enter second number:"))
print(f0)
print(f1)
for i in range(1,num-1):
    f=f0+f1
    f0=f1
    f1=f
    print(f)
