# list comprehensions
# it's a case were you create list from an old list:

# new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
# print(new_list)

name = "aaryan"
new_list1 = [letter for letter in name]
print(new_list1)

numbers1 = range(1, 5)
new_numlist = [2*n for n in numbers1]
print(new_numlist)

# conditional list comprehension
# new_list = [new_item for item in list if test]

nice = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']

short_name = [name for name in nice if len(name) < 5]
print(short_name)
cap_name = [name.upper() for name in nice if len(name) > 4]
print(cap_name)