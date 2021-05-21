#python script to compute various areas of geometrical figures
def circle():
    r=float(input("Enter the radius:"))
    a=3.14*r*r
    print("Area of circle is",a)

def rectangle():
    l=float(input("Enter the length"))
    b=float(input("Enter the breadth"))
    a=l*b
    print("Area of rectangle is",a)

def triangle():
    b=float(input("Enter base:"))
    h=float(input("Enter height:"))
    a=0.5*b*h
    print("Area of triangle is",a)

def square():
    l=float(input("Enter length:"))
    a=l*l
    print("Area of square is",a)
