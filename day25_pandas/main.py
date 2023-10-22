
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# tables in general are referred to as Dataframes.
print(data)

# print(type(data["temp"]))
# a column in a table or a list is referred to as a series.

data_dict = data.to_dict()

print(data_dict)

temp_list = data_list = data["temp"].to_list()
print(temp_list)
# sum = 0
# for value in temp_list:
#     sum = sum+value
    # or we could just simply use sum() function

# avg = sum/len(temp_list)
#
# print(avg)

# or we could just
print(data["temp"].mean())
print(data["temp"].max())
# print(data["condition"])
# print(data.condition)
# it is basically the same as using "condition"

# all of these are for columns

print(data[data.day == "Monday"])
# this gives access to the entire row of "Monday"

print(data[data.temp == data["temp"].max()])

sunday = data[data.day == "Sunday"]
print(sunday.condition)

monday = data[data.day == "Monday"]

sun_feren = (sunday.temp*9/5) + 32
print(sun_feren)

mon_feren = (monday.temp[0]*9/5) + 32
print(mon_feren)

# create a dataframe from scratch:

stud_dic = {
    "students": ["aaryan", "nedjem", "luluu"],
    "marks": [54, 67, 88]
}

new_data = pandas.DataFrame(stud_dic)

print(new_data)
new_data.to_csv("auto_data.csv")