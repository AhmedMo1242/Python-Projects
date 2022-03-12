import random

def game():
    game_on = True
    while game_on:
        Choice = " "
        Continue_Game = " "
        while Choice != 's' and Choice != 'p' and Choice != 'r':
            Choice = input("What's your choice ? 'r' for rock 'p' for paper 's' for scissors : ") 
            if Choice != 's' and Choice != 'p' and Choice != 'r':
                print("please enter valid letter")
            Computer_Choice = random.choice(['s','r','p'])
                
        if Computer_Choice == Choice: 
            print("Tie")

        elif Win(Choice,Computer_Choice):
            print("You wins")
    
        else :
            print("You loses")
            
        while Continue_Game != 'y' and Continue_Game != 'n':
            Continue_Game = input("Do you want to play again? 'y' for yes, 'n' for no")
            if Continue_Game != 'y' and Continue_Game != 'n':
                print("Please Enter valid letter")
            
            if Continue_Game == 'n':
                game_on = False
                print("game over")
            elif Continue_Game == 'y' :
                game_on = True
    
def Win(Choice,Computer_Choice):
    if (Choice == 'p' and Computer_Choice == 'r')or (Choice == 'r' and Computer_Choice == 's') or  (Choice == 's' and Computer_Choice == 'p'):
        return True
    
game()