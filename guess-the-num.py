import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Sorry, try again. Too high!")
        elif guess < random_number:
            print("Sorry, try again! Too low!")
            
    print (f"Yay, great job! You've guess the number {random_number} correctly.")
        
guess(20)
    