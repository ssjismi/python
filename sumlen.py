n1=input("enter a 1st list of integers separated by space")
n2=input("enter a 2nd list of integers separated by space")
n1int=list(map(int,n1.split()))
n2int=list(map(int,n2.split()))
if len(n1int)==len(n2int):
    print("both are of same length")
else:
    print("diff length")
if sum(n1int)==sum(n2int):
    print("both have same sum values")
else:
    print("diff sum values")
common_values=set(n1int)&set(n2int)
if common_values:
    print("same values occur")
else:
    print("no same values")
