# from replit import clear
# HINT: You can call clear() to clear the output in the console.

# from art import logo
# print(logo)

bidders = {}
bidding_finished = False


def highest_bidder(bidding_record):
    highest_bid = 0
    # bidding_record = {"aaryan": 345,.....}
    for bidder in bidding_record:
        bid = bidding_record[bidder]
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder

    print(f"The winner is {winner} with ${highest_bid}.")


print("Welcome to the secret auction program.")
while not bidding_finished:
    name = input("What is your name?:")
    price = int(input("What is your bid?: $"))
    # in the dictionary the key is name, the value is price
    bidders[name] = price
    conti = input("Are there any other bidders ?, type 'yes' or 'no': ")
    if conti == "no":
        bidding_finished = True
        highest_bidder(bidders)
    elif conti == "yes":
        # clear()
        print("clear the screen using clear() function.")
