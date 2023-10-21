#
# import pandas
#
# phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
# # print(phonetic.to_dict())
#
# # {new_key: new_value for (index, row) in df.iterrows()}
# phonetic_dict = {row.letter: row.code for (index, row) in phonetic.iterrows()}
# # print(phonetic_dict)
#
# word = input("Enter a word: ").upper()
#
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)

# day 30: exceptions (error handling)

import pandas

phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(phonetic.to_dict())

# {new_key: new_value for (index, row) in df.iterrows()}
phonetic_dict = {row.letter: row.code for (index, row) in phonetic.iterrows()}
# print(phonetic_dict)

def gen_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please enter letters only.")
        gen_phonetic()
    else:
        print(output_list)

gen_phonetic()

