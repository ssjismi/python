dic={}
n=int(input("enter the no.of kay,val pairs"))
for i in range (n):
    key=input("enter the key:")
    val=input("enter the val:")
    dic[key]=val
print(dic)
for key,val in dic.items():
    print(f"{key}:{val}")
dic1={}
n1=int(input("enter the no.of kay,val pairs"))
for i in range (n1):
    key=input("enter the key:")
    val=input("enter the val:")
    dic1[key]=val
for key,val in dic1.items():
    print(f"{key}:{val}")
dic.update(dic1)
print(dic) 
