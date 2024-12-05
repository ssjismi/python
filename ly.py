while True:
    s=input("enter a string(or type 'exit' to quit)")
    if s=='exit':
        break
    if(s[-3:]=='ing'):
        n2=s+'ly'
        print(n2)
    else:
        n3=s+'ing'
        print(n3)
