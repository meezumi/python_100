from random import *
from game_data import *
from art import *
import random

print(logo)

p1 = random.choice(data)
score = 0

game_end = False
while not game_end:
  p2 = random.choice(data)
  if p1 == p2:
      p2 = random.choice(data)

  print("Compare A: " + p1["name"] + ", a " + p1["description"] + ", from " + p1["country"] + ".")

  print(vs)

  print("Against B: " + p2["name"] + ", a " + p2["description"] + ", from " + p2["country"] + ".")

  user_choose = input("Who has more followers? Type 'A' or 'B':").lower()

  if p1["follower_count"] > p2["follower_count"] and user_choose == "a":
      score += 1
      print(f"Your Current Score: {score}.")

  elif p2["follower_count"] > p1["follower_count"] and user_choose == "b":
      score += 1
      print(f"Your Current Score: {score}.")
      p1 = p2
  else:
      print(f"Your Final Score: {score}.")
      game_end = True
