# Falty calculator
# Falts are the following once:
# 45+3=555, 56+9=77, 56/6=4

def calculator(a,b):
    print("choose any one: ")
    print(" press 1 to add\n press 2 to subtract\n press 3 to multipy\n press 4 to divition")
    n=int(input("What do you want to do?\n "))
    flag=0
    if n==1:
        if a==45 and b==3:
            print(555)
            flag=1
        if flag==0:    
            if a==56 and b==9:
                print(77)
                flag=1
        if flag==0:
            add = a+b
            print("Your sum is ",add)
        
    elif n==2:
        sub = a-b
        print("Your subtraction is ",sub)
    elif n==3:
        mul = a*b
        print("Your multiplication is ",mul)
    elif n==4:
        if a==56 and b==6:
            print(4)
            flag=1
        if flag==0:
            div = a/b
            print("Your divition is",div)
    else:
        print("Sorry your input is wrong")
def again():
    while True:
        print("Do you want to play again?\n")
        ans= input(" If yes eneter Y\n if no enter N ")
        if ans=="Y":
            x=int(input("Enter value of a:- "))
            y=int(input("Enter value of b:- "))
            calculator(x,y)
        elif ans=="N":
            print("Thankyou (-_-)")
            break
        else:
            print("Your input is wrong enter Y/N\n ")
a=int(input("Enter value of a:- "))
b=int(input("Enter value of b:- "))
calculator(a,b)
again()            
