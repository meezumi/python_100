# import random 
# import my_module_day4 

# random_int = random.randint(1,10)
# print(random_int)

# print(my_module_day4.pi) this can be used to import your own created module in this py file 

# import random

# random_float = random.random()*5
# print(random_float)

# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}%")

# cointoss = random.randint(0,1)
# print(cointoss)

# LISTS

# statesofamerica = ["Deewfw","wuwfhw","wfuwhfow"]

# print(statesofamerica[-1]) # -1 gives u the last item of the list and if u keep decreasing it it givesoutput backwords.
# statesofamerica[0] = "wfiuhwfuh" # u can also change the first item of that list whenever u want to.
# print(statesofamerica[0])
# statesofamerica.append("angelaland") # append will add a single item at the end of the list.
# print(statesofamerica[-1])
# statesofamerica.extend(["wfuwhfiw","wifuhwiufh","Aaryan"]) # whereas extend will add another list to that existing list.
# print(statesofamerica[-1])

# NESTED LISTS 

# one = ["wfoijw","woufhw","wfowiod"]
# two = ["wiur3oif","wifuoif","wofijwf"]
# dirty_dozen = [one,two]
# print(dirty_dozen)
# print(dirty_dozen[0])
# print(dirty_dozen[1][1])

# CODING EXERCISE 4.3 TREASURE MAP 

#  Don't change the code below 
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#  Don't change the code above 

#Write your code below this row 

hori=int(position[0])
verti=int(position[1])
print(map[verti-1])
#Write your code above this row 

#  Don't change the code below 
print(f"{row1}\n{row2}\n{row3}")




