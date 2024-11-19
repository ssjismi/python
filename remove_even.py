n=input("enter a list of numbers separeted by space")
l=list(map(int,n.split()))
l1=[]
for i in l:
    if i%2!=0:
        l1.append(i)
print(l1)
