import turtle
import pandas

data = pandas.read_csv("50_states.csv")
# print(state_data)
all_states = data.state.to_list()


screen = turtle.Screen()
screen.title("U.S State Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# gonna keep over window open

# if state_data is one of the states of the 50,
    # if its right:
        # create a turtle and move it to its states coordinate.

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        # this is called comprehension
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        print(missed_states)

        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # by default, they must be in string, so we have to convert it to int
        t.write(answer_state)

        # or t.write(state_data.state.item())

