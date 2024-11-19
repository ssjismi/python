uin=input("enter a list of numbers separated by spaces")
input_list = list(map(int,uin.split()))
L=[]
for num in input_list:
    if num>100:
        L.append('over')
    else:
        L.append(num)
print(L)
