import random
print("******lets start the game******")
name=input("Enter your name:")
print("CHOOSE\n1.Hard(chances=3)\n2.Medium(chances=5)\n3.Easy(chances=7)\n")
choice=int(input("which level do you want to play:"))
number=random.randint(1,10)
chance=0
flag=0
result=0
if(choice<=3 and choice!=0):
    while chance<=choice*2:
        guess=int(input("Guess the number:"))
        chance=chance+1
        if(guess==number):
            print("u won the game in",chance,"chances")
            flag=1
            break;
        elif(guess==number):
            print("\t")
        else:
            print("\tRETRY")
else:
    print("\tINVALID CHOICE")
if(flag==0):
    print("\tU LOST THE GAME!!!!\n\tThe correct answer is",number)
