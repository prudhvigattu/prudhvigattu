#python script to print all the digits in a given number

n=int(input("Enter a number:"))
print("The digits in the given number is")

temp=n
while(n!=0):
    rem=n%10
    print(rem)
    n=n//10
