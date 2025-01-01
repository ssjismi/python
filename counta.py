a=input("enter the names comma separated:")
b=[name.strip() for name in a.split(',')]
counta=0
for name in b:
        counta+=name.count('a')
print(counta)
