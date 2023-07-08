MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resource(order_ingredients):
  """Before making the coffee, checking if the ingredients are available."""
  for item in order_ingredients:
    if order_ingredients[item] >= resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False # to exit the function
  return True

def process_coins():
  print("Please insert coins: ")
  quaters = int(input("Enter quaters ($0.25/coin):"))
  dimes = int(input("Enter dimes ($0.10/coin):"))
  nickles = int(input("Enter nickles ($0.05/coin):"))
  pennies = int(input("Enter pennies ($0.01/coin):"))
  total = float(quaters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01)
  print(total)
  return total

def trans_success(payment, drink_cost):
  if payment >= drink_cost:
    change = round(payment - drink_cost, 2)
    print(f"Here is your change: ${change}.")
    global profit
    profit += drink_cost
    return True
  else:
    print("Sorry, not enough money. Money refunded.")
    return False
  
def make_coffee(drink_name, order_ingredients):
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]

  print(f"Here is your {drink_name}. Enjoy!")

is_on = True
while is_on:
  user_choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
  if user_choose == "off":
    is_on = False
  elif user_choose == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

  elif user_choose == "resupply":
    resources["water"] == 300
    resources["milk"] == 200
    resources["coffee"] == 100

  else:
    drink = MENU[user_choose]
    if check_resource(drink["ingredients"]):
      payment = process_coins()
      if trans_success(payment, drink["cost"]):
        make_coffee(user_choose, drink["ingredients"])