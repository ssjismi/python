n=input("Enter the 1st list of colors comma separated")
n1=input("Enter the 2nd list of colors")
c1=n.split(',')
c2=n1.split(',')
pr=list(set(c1)-set(c2))
print(pr)
