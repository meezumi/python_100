# import logo from art

def add (n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

operations = { # "key": value,
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

# recursion is function calling itself 

def calculator():
  # print(logo)
  num1 = float(input("enter a number: "))

  for symbol in operations:
      print(symbol)

  carry_on = True
  while carry_on:
    operation_symbol = input("Pick an operation: ")

    num2 = float(input("choose the next number: "))

    function = operations[operation_symbol]
    answer = function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    yeyy = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if yeyy == "y":
        num1 = answer
    else:
        carry_on = False
        calculator()

calculator()