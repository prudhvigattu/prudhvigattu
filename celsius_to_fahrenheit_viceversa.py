#python script to convert celsius to fahrenheit and vice-versa

def ctof():
    c=float(input("enter Celsius temperature:"))
    f=(c*(9/5))+32
    print("fahrenheit temperature is",f)

def ftoc():
    f=float(input("Enter fahrenheit temperature:"))
    c=(f-32)*(5/9)
    print("celsius temperature is",c)
    
