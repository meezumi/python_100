sum = 0

for number in range(1, 101):
    # range(1, 101, 2) means that it will increase in two steps starting from 1 so 1,3,5....
    if number % 2 == 0:
        sum = sum + number

##############################################################

print(sum)

marks = [23, 1123, 212, 444, 2131, 1313123, 111, 333, 1112]
max = 0
for mark in marks:
    if mark > max:
        max = mark

print(max)

##############################################################

for number in range(1, 100):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
