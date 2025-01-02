dic={}
n=int(input("enter the no of key,value pairs:"))
for i in range (n):
    key=input("enter the key: ")
    val=input("enter the value:")
    dic[key]=val
print("\n contents of dictionary")
for key,val in dic.items():
    print(f"{key}:{val}")
