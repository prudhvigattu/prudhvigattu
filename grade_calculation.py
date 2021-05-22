#python program on grade calculation
def grade():
    m=int(input("enter marks:"))
    if m>=75 and m<=100:
        print("First class with distinction")
    elif m>=60 and m<75:
        print("Second class")
    elif m>=50 and m<60:
        print("third class")
    elif m>=0 and m<50:
        print("fail")
    else:
        print("invalid marks")
        
