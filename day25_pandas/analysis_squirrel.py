import pandas

# grey, cinamon, black suirrels

data = pandas.read_csv("squirrel_data.csv")
# print(data)

gray = len(data[data["Primary Fur Color"] == "Gray"])
# print(gray)
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(cinnamon)
black = len(data[data["Primary Fur Color"] == "Black"])
# print(black)

squireel = {
    "color": ["gray", "cinnamon", "black"],
    "numbers": [gray, cinnamon, black]
}

# print(squireel)

create_csv = pandas.DataFrame(squireel)
print(create_csv)

create_csv.to_csv("squirrel_nice.csv")

# for color in data:
#     if(data[data["Primary Fur Color"] == "Gray"]):
#         gray += 1
#
#     elif(data[data["Primary Fur Color"] == "Black"]):
#         black += 1
#
#     elif(data[data["Primary Fur Color"] == "Cinnamon"]):
#         cinnamon += 1
#
# print(gray)
