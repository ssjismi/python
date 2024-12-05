side=2
height=2
base=3
length=4
width=1
square=lambda side:side**2
rectangle=lambda length,width:length*width
triangle=lambda base,height:0.5*base*height
print("Area of square:",square(side))
print(f"Area of rectangle:{rectangle(length, width)}")
print(f"Area of triangle:{triangle(base, height)}")

