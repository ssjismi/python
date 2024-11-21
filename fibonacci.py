n=int(input("enter a number"))
a,b=0,1
print(a)
for i in range (0,n+1):
    a,b=b,a+b
    print(a)
