import random
# from art import logo
# from replet import clear

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2: # represent a blackjack
     return 0
  if 11 in cards and sum(cards) > 21:
     cards.remove(11)
     cards.append(1)

  return sum(cards)


def compare(user_score, computer_score):
   if user_score == computer_score:
      return "Draw"
   elif computer_score == 0:
      return "Lose, Computer has BlackJack."
   elif user_score == 0:
      return "Win with a BlackJack."
   elif user_score > 21:
      return "Over 21, You Lose."
   elif computer_score > 21:
      return "Opponent Over 21, You Win."
   elif user_score > computer_score:
      return "You Won"
   else:
      return "You Lose"
   
def play_game():
  # print(logo)
  user_cards = [] 
  computer_cards = []
  game_over = False

  i = 0
  while i != 2:
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    i+=1

  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f" your cards: {user_cards}, current score: {user_score}")
    print(f" computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      more = input("Type 'y' to get another card, type 'n' to pass: ")
      if more == "y":
          user_cards.append(deal_card())
      else:
          game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your Final Hand: {user_cards}, Final Score: {user_score}.")
  print(f"Computer's Final Hand: {computer_cards}, Final Score: {computer_score}.")

  print(compare(user_score, computer_score))

while input("Press 'y' to play or 'n' to exit: ") == "y":
  #  clear()
   play_game()
