#data types 

# from operator import ne


# print("Hello"[4])
# # this is used to display the letter of the string.

# print("123" + "456")
# # this would just print 123456

# #integers

# print(123+456)
# #will add

# 123_234_456 
#the computer will treat this as 123234456

# adding a stg to an int is just not possible. so to fix that we

# num_char=len(input("What is your name? "))

# newnum_char=str(num_char)

# print("your name has " + newnum_char + " characters. ")

# a=123
# print(type(a))
# #  Don't change the code below 
# two_digit_number = input("Type a two digit number: ")
# #  Don't change the code above 

# print(int(two_digit_number[0])+int(two_digit_number[1]))

# ** is used to raise to power

# print(3*(3 + 3)/3 - 3)

# rounding off a number 

# print(round(2.766666,3))

# f-str (MOST IMPORTANT THING TILL NOW)

# score = 1
# height = 4
# we_wennin= True
# print(f"your score is {score}\nyour height is {height} \n{we_wennin} that you are winning")



print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("What much tip would you like to give? 10, 12 or 15 ? "))
people=int(input("How many people to split the bill? "))
tip_per_person=("{:.2f}".format(round(float((bill/people)*(1+(tip/100))),2)))
print(f"Each person should pay: ${tip_per_person}")






