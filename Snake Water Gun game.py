import random
def computer_choice():
    print("Player2")
    choice_ans = ['snake','water','gun']
    ans=random.choice(choice_ans)
    return ans
def my_choice():
    print("Player1")
    print("Choose any one:\n snake\n water\n gun\n")
    ans=input("Press 'S' for snake, press 'W' for water, press 'G' for gun\n")
    return ans
def game_rule(my_choice,computer_choice):
    c_point=0
    m_point=0
    if computer_choice=='snake' and my_choice=='W':
        c_point=c_point+1
    if my_choice=='S' and computer_choice=='water':
        m_point=m_point+1
    if computer_choice=='snake' and my_choice=='G':
        m_point=m_point+1
    if my_choice=='S' and computer_choice=='gun':
        c_point=c_point+1
    if computer_choice=='water' and my_choice=='G':
        c_point=c_point+1
    if my_choice=='W' and computer_choice=='gun':
        m_point=m_point+1
    print(f'Computer points is: {c_point}\nmy points is: {m_point}')
print("Game starts now......")
x=0
c_point=0
m_point=0
Round =0
while x<5:
    print('--------------------------------------------------------------------------------')
    my_choice1=my_choice()
    computer_choice1=computer_choice()
   
    #result=game_rule(player1,player2)
    #print(result)
    
    #print("Computer point: ",c_point)
    #print("My point: ",m_point)
    
    if computer_choice1=='snake' and my_choice1=='W':
        c_point=c_point+1
        print("Computer point 1")
    if my_choice1=='S' and computer_choice1=='water':
        m_point=m_point+1
        print("my point 1")
    if computer_choice1=='snake' and my_choice1=='G':
        m_point=m_point+1
        print("My point 1")
    if my_choice1=='S' and computer_choice1=='gun':
        c_point=c_point+1
        print("Computer point 1")
    if computer_choice1=='water' and my_choice1=='G':
        c_point=c_point+1
        print("Computer point 1")
    if my_choice1=='W' and computer_choice1=='gun':
        m_point=m_point+1
        print("My point 1")
    if my_choice1=='s' and computer_choice1 =='snake':
        print("----------------Bingoooooooo----------")
    if my_choice1=='G' and computer_choice1 == 'gun':
        print("----------------Bingoooooooo----------")
    if my_choice1=='W' and computer_choice1 =='water':
        print("----------------Bingoooooo------------")
    
    x+=1
print()    
print("Total points ")    
print(f'Computer points is: {c_point}\nmy points is: {m_point}')    
