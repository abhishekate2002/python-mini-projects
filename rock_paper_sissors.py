import random  
game = ["rock", "paper", "scissors"]  
print("Welcome to rock paper scissors!")  
print("Select your move first")  
user_move = int(input("0 for rock, 1 for paper, 2 for scissors: "))  
computer_move = random.randint(0,2)  
statement =  f"Your move: {user_move} and computer move: {computer_move}."  
if user_move == computer_move:  
    print(statement)  
    print("It's a tie!")  
elif user_move == 0 and computer_move == 2:  
    print(statement)  
    print("you  won")  
elif user_move == 1 and computer_move == 0:  
    print(statement)  
    print("you  won")  
elif user_move == 2 and computer_move  == 1:  
    print(statement)  
    print("you  won")  
else:  
    print(statement)  
    print("You lost")
