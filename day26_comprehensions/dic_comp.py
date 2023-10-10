# dictionary comprehension
import random
import pandas
# new_dict = {new_key: new_value for item in list}

# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

names = ['aaryan', 'gungun', 'khyaati', 'beth', 'alex', 'pratyush']

students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)

passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
# print(passed_students)

student_dict = {
    "student": ["aaryan", "james", "lily"],
    "score": [56, 76, 98]
}

#looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)
#     print(key)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(key)

# loop through rows of a data frame
for(index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.score)
    if row.student == "aaryan":
        print(row.score)