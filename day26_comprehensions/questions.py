# list_of_strings = input().split(',')
# # 🚨 Do  not change the code above
#
# # TODO: Use list comprehension to convert the strings to integers 👇:
# numbers = [int(num) for num in list_of_strings]
# # TODO: Use list comprehension to filter out the odd numbers
# # and store the even numbers in a list called "result"
# result = [num for num in numbers if num%2 == 0]
#
# # Write your code 👆 above:
# print(result)



# file1 = open("file1.txt")
# file2 = open("file2.txt")
# contents1 = file1.readlines()
# num1 = [num.strip() for num in contents1]
# n1 = [int(num) for num in num1]
#
# contents2 = file2.readlines()
# num2 = [num.strip() for num in contents2]
# n2 = [int(num) for num in num2]
#
# result = [num for num in n1 if num in n2]



# sentence = input()
# # 🚨 Don't change code above 👆
# # Write your code below 👇
# words = sentence.split()
# # print(words)
#
# result = {word: len(word) for word in words}
# # print(new_dict)
# print(result)



# weather_c = eval(input())
# # 🚨 Don't change code above 👆
#
# # Write your code 👇 below:
#
# weather_f = {day: (temp*9/5) + 32 for (day, temp) in weather_c.items()}
# print(weather_f)



