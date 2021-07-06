# enter choice for student
print("Choose any one student")
stu  = int(input(" press 1 to harry\n press 2 to rohan\n press 3 to hammad\n ")) 
# rnter choise for work
work = int(input("Choose any one work\n press 1 to diet\n press 2 to exercise\n "))
# if press 1 it will work
if stu==1:
    # diat
    if work==1:
        # open file
        f=open("harray_dait.txt.txt")
        for line in f:
            print(line,end="")
        print("\n")
            
        # to ask add diet or not
        print("Do you want to add diet?")   
        ans=input("press Y to add diet\npress N to not intrusting to add diet\n")
        if ans== "Y":
            # To add diet
            add_diet = input("Please enter your diet\n")
            f=open("harray_dait.txt","a")
            f.write(str(str([getdate()])) + ": "+ add_diet+ "\n")
            ans1=int(input("press 1 to show your diet status\n press 2 to not intrusted\n"))
            if ans1==1:
                f=open("harray_dait.txt")
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()
            if ans1==2:
                # ask to close diet
                print("Do you want to close diet or not")
                ans2=input("press Y to yes\n press N to not")
                if ans2=="Y":
                    f.close()
                else:
                    print("Thankyou")
                
        if ans=='N':
            # ask to show diet status or lock diet
            ans1=int(input("press 1 to show your diet status\n press 2 to close your diet\n"))
            # To show diet status 
            if ans1==1:
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()

            # To close diet status   
            if ans1==2:
                f.close()  
                
    # exercise      
    if work==2:
        f=open("harry_exercise.txt")
        for line in f:
            print(line,end="")
        print("\n")
        # to ask add exercise or not
        print("Do you want to add exercise?")   
        ans=input("press Y to add exercise\npress N to not intrusting to add exercise\n")
        if ans== "Y":
            # To add exercise
            add_exercise = input("Please enter your exercise\n")
            f=open("harry_exercise.txt","a")
            #f.write(add_exercise)
            f.write(str(str([getdate()])) + ": "+ add_exercise+ "\n")
            ans1=int(input("press 1 to show your exercise status\n press 2 to not intrusted\n"))
            if ans1==1:
                f=open("harry_exercise.txt")
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()
            if ans1==2:
                # ask to close exercise
                print("Do you want to close exercise or not")
                ans2=input("press Y to yes\n press N to not")
                if ans2=="Y":
                    f.close()
                else:
                    print("Thankyou")
                
        if ans=='N':
            # ask to show exercise status or lock exercise
            ans1=int(input("press 1 to show your exercise status\n press 2 to close your exercise\n"))
            # To show exercise status 
            if ans1==1:
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()

            # To close exercise status   
            if ans1==2:
                f.close()  
                

# if press 2 it will work                        
if stu==2:
    # diet
    if work==1:
        f=open("rohan_dait.txt")
        for line in f:
            print(line,end="")
        print("\n")
        # to ask add diet or not
        print("Do you want to add diet?")   
        ans=input("press Y to add diet\npress N to not intrusting to add diet\n")
        if ans== "Y":
            # To add diet
            add_diet = input("Please enter your diet\n")
            f=open("rohan_dait.txt","a")
            f.write(str(str([getdate()])) + ": "+ add_diet+ "\n")
            ans1=int(input("press 1 to show your diet status\n press 2 to not intrusted\n"))
            if ans1==1:
                f=open("rohan_dait.txt.txt")
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()
            if ans1==2:
                # ask to close diet
                print("Do you want to close diet or not")
                ans2=input("press Y to yes\n press N to not")
                if ans2=="Y":
                    f.close()
                else:
                    print("Thankyou")
                
        if ans=='N':
            # ask to show diet status or lock diet
            ans1=int(input("press 1 to show your diet status\n press 2 to close your diet\n"))
            # To show diet status 
            if ans1==1:
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()

            # To close diet status   
            if ans1==2:
                f.close()  
    
    # exercise        
    if work==2:
        f1=open("rohan_excercise.txt")
        for line in f1:
            print(line,end="") 
        print("\n")
        # to ask add exercise or not
        print("Do you want to add exercise?")   
        ans=input("press Y to add exercise\npress N to not intrusting to add exercise\n")
        if ans== "Y":
            # To add exercise
            add_exercise = input("Please enter your exercise\n")
            f=open("rohan_excercise.txt","a")
            #f.write(add_exercise)
            f.write(str(str([getdate()])) + ": "+ add_exercise+ "\n")
            ans1=int(input("press 1 to show your exercise status\n press 2 to not intrusted\n"))
            if ans1==1:
                f=open("rohan_excercise.txt")
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()
            if ans1==2:
                # ask to close exercise
                print("Do you want to close exercise or not")
                ans2=input("press Y to yes\n press N to not")
                if ans2=="Y":
                    f.close()
                else:
                    print("Thankyou")
                
        if ans=='N':
            # ask to show exercise status or lock exercise
            ans1=int(input("press 1 to show your exercise status\n press 2 to close your exercise\n"))
            # To show exercise status 
            if ans1==1:
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()

            # To close exercise status   
            if ans1==2:
                f.close()  
        

# if press 3 it will work            
if stu==3:
    # diet
    if work==1:
        f=open("hammad_dait.txt")
        for line in f:
            print(line,end="")
        print("\n") 
        # to ask add diet or not
        print("Do you want to add diet?")   
        ans=input("press Y to add diet\npress N to not intrusting to add diet\n")
        if ans== "Y":
            # To add diet
            add_diet = input("Please enter your diet\n")
            f=open("hammad_dait.txt","a")
            f.write(str(str([getdate()])) + ": "+ add_diet+ "\n")
            ans1=int(input("press 1 to show your diet status\n press 2 to not intrusted\n"))
            if ans1==1:
                f=open("hammad_dait.txt.txt")
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()
            if ans1==2:
                # ask to close diet
                print("Do you want to close diet or not")
                ans2=input("press Y to yes\n press N to not")
                if ans2=="Y":
                    f.close()
                else:
                    print("Thankyou")
                
        if ans=='N':
            # ask to show diet status or lock diet
            ans1=int(input("press 1 to show your diet status\n press 2 to close your diet\n"))
            # To show diet status 
            if ans1==1:
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()

            # To close diet status   
            if ans1==2:
                f.close()
    # exercise
    if work==2:
        f1=open("hammad_exercise.txt")
        for line in f1:
            print(line,end="")   
        print("\n")
        # to ask add exercise or not
        print("Do you want to add exercise?")   
        ans=input("press Y to add exercise\npress N to not intrusting to add exercise\n")
        if ans== "Y":
            # To add exercise
            add_exercise = input("Please enter your exercise\n")
            f=open("hammad_exercise.txt","a")
            #f.write(add_exercise)
            f.write(str(str([getdate()])) + ": "+ add_exercise+ "\n")
            ans1=int(input("press 1 to show your exercise status\n press 2 to not intrusted\n"))
            if ans1==1:
                f=open("hammad_exercise.txt")
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()
            if ans1==2:
                # ask to close exercise
                print("Do you want to close exercise or not")
                ans2=input("press Y to yes\n press N to not")
                if ans2=="Y":
                    f.close()
                else:
                    print("Thankyou")
                
        if ans=='N':
            # ask to show exercise status or lock exercise
            ans1=int(input("press 1 to show your exercise status\n press 2 to close your exercise\n"))
            # To show exercise status 
            if ans1==1:
                f.seek(0)
                for line in f:
                    print(line,end="")
                print()

            # To close exercise status   
            if ans1==2:
                f.close() 
              
    
