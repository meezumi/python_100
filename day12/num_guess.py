from random import *

number = randint(1,100) # randint is inclusive of the boundaries 

def guess_game(chances):
  global number
  game_end = False
  chance = chances 
  while not game_end:
    print(f"You have {chance} attempts remaining to guess the number.")  
    user_guess = int(input("Make a guess:"))
    if user_guess > number:
      print("Too High.")
      chance -= 1
    elif user_guess < number:
      print("Too Low.")
      chance -= 1
    elif user_guess == number:
      print(f"Yes! the Number was {number}, You Won!!")
      game_end = True
      if chance == 0:
        print("Out of Attempts, You Lose!")
        game_end = True
   

print("Welcome to the Number Guessing Game!")
print("I'm thinking a number between 1 to 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'hard':
  guess_game(5)
elif difficulty == 'easy':
  guess_game(10)


    
        



