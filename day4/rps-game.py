import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# writing my code logic beginning from here //

input_img = [rock, paper, scissors]

player = int(input("1 for Rock, 2 for Paper and 3 for Scissor:\n"))
print(input_img[player])

computer = random.randint(0, 2)
print(input_img[computer])

if player >= 3 or player < 0:
    print("Invalid Input")
elif player == 0 and computer == 1:
    print("You Lose!")
elif player == 1 and computer == 2:
    print("You Lose!")
elif player == 2 and computer == 0:
    print("You Lose!")
elif player == computer:
    print("It's a Draw!")
else:
    print("You Win")
