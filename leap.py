def leap(year):
    return(year%4==0 and year%100!=0)or(year%400==0)
import datetime
current=datetime.datetime.now().year
print(f"current year:{current}")
final=int(input("enter the final year"))
print("future leap years are:")
for year in range(current,final+1):
    if leap(year):
        print(year)
