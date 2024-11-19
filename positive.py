n=input("enter a list of integers comma separated:")
n1=list(map(int,n.split(',')))
l=[]
for i in n1:
    if i>=0:
        l.append(i)
print(l)   
