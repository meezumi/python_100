# from ast import If


# height =int(input("What is your height?"))
# bill=0

# if height >= 120:
#   print("u high")
#   age=int(input("ur age? "))
#   if age<12:
#     bill=5
#   elif age <=18:
#     bill=7
#   elif age >=45 and age <=55:
#     print("Have a free ride on us!.")
#   else:
#     bill=12
#   photo_want=input("Do you want a photo taken? Y or N.")
#   if photo_want=="Y":
#     bill+=3
#     print(f"that would be {bill}$ please") 
#   else:
#     print(f"that would be {bill}$ please.")

# else:
#   print("u shorty")

from calendar import c


print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print(f"Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice1=input('You\'re at a crossroad, where do you want to go? type "Left" or "Right".').lower()
if choice1 == "left":
  choice2=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross.').lower()
  if choice2 == "wait":
    choice3=input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yello and one blue. Which colour do you choose? ").lower()
    if choice3 == "yellow":
      print(f"It's a room full of treasure. Congrats!! You have found the treasure.")
    elif choice3 == "red":
      print(f"It's a room full of fire. Game Over.")
    elif choice3 == "blue":
      print(f"It's a room full of beasts. Game Over.")
    else:
      print("you chose a door that doesn't exists. Game Over.")

  else:
    print("You got attacked by a hungry tiger. Game Over.")
elif choice1 == "right":
  print(f"You fell into the hole. Game Over.")
else:
  print("You don't even know how to write what you are asked properly. Game Over.")




