import random

#Guessing the number by the user

def guess(x,y):
    random_number = random.randint(x,y)
    guess = 0 
    while guess != random_number: 
        guess = int(input("Choose Number berween {} and {} : ".format(x,y)))
        if guess not in range(x,y):
            print("This Number isn't in the range")
        elif guess > random_number : 
            print("Your Guess is larger than The number")
        elif guess < random_number :
            print("Your Guess is less than the number")
    print("Congrats, You got the number right")
    
x = int(input("The Minimum Number in the random range : "))
y = int(input("The Maximum Number in the random range : "))
guess(x,y)

#Guessing the number by the computer

def computer_guess(x,y,z):
    Correct_answer = z
    while z not in range(x,y):
        print('Your Answer is not in the range')
        break
    random_number = 0
    while random_number != Correct_answer: 
        random_number = random.randint(x,y)
        print("The Number computer guessed is : {} ".format(random_number))
        if random_number > Correct_answer : 
            print('The Number Computer guessed is larger than the answer')
            y = random_number
        elif random_number < Correct_answer:
            print("The Number Computer guessed is less than the answer")
            x = random_number
    print("Computer Guessed your number right")
x = int(input("The Minimum Number in the random range : "))
y = int(input("The Maximum Number in the random range : "))
z = int(input("The answer that computer should guessed is : "))
computer_guess(x,y,z)