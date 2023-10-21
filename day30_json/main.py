# with open("a_file.txt") as file:
#     file.read()

# try: something that might cause an exception
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["sbduss"])
#
# # except: do this if there was an exception
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_mess:
#     print(f"That key {error_mess} does not exist.")
#
# # else: do this if there were no exceptions
# else:
#     content = file.read()
#
# # finally: do this no matter what happens
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError("This is an error that i made up.")

height = float(input("Height(in m): "))
weight = int(input("Weight(in kg): "))

if height > 3:
    raise ValueError("Human Height should not be more than 3 metres")

bmi = weight / height ** 2
print(bmi)

