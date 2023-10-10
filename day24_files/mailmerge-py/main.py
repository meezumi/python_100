    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
PLACEHOLDER = "[name]" # in the starting_letter file
        
with open("./day24_files/mailmerge-py/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines() # readlines create each line in the txt file as a list.
    print(names)
    
with open("./day24_files/mailmerge-py/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read() 
    for name in names: # name in the names list
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name) # replace functiong helps replace a part with some other word or sentence 
        print(new_letter)
        with open(f"./day24_files/mailmerge-py/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
        
        