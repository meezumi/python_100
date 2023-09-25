
# file = open("./day24_files/my_file.txt")
# # opens the file 

# contents = file.read()
# # reads the file

# print(contents)
# # prints the content of the file 

# file.close()
# close the file manually to free the resources 

# to automatically close the file we use: with and as

with open("./day24_files/my_file.txt", mode="r") as file:
  # file is set to read only, specifying r the mode 
  contents = file.read()
  print(contents)
  
  
with open("./day24_files/my_file.txt", mode="a") as file:
  # file is set to write, specifying w in the mode
  # so it will remove everything in the file and paste this, to add we use append (a)
  file.write("\nNew text.") 
  
with open("./day24_files/new_file.txt", mode="w") as file:
  # if file already not created its gonna make one for you, only works in write mode 
  file.write("new text.") 