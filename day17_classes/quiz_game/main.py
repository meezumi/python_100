from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
  question_text = question["question"]
  question_answer = question["correct_answer"]
  new_question = Question(question_text, question_answer)
  question_bank.append(new_question)
  
# print(question_bank) 
#  will print the address of the questions where they are stored 

# print(question_bank[0].question)
# prints the first question 

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
  quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# we can add more questions from open trivia database https://opentdb.com/api_config.php