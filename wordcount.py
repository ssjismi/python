n=input("enter a string")
n1=n.split()
count={}
for word in n1:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
for word,count in count.items():
    print(f"{word}:{count}")
