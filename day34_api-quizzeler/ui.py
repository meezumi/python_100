from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="some question text",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=35)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel", 10))
        self.score_label.grid(column=1, row=0)

        self.right_but_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_but_img, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(column=0, row=2)

        self.wrong_but_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_but_img, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The Quiz is finished :)")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        # is_right = self.quiz.check_answer("False")
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)

