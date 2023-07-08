def myfunc():
    print("hello")
    print("bye")


myfunc()


# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# Hurdle 1

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def finish():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for step in range(1,7):
#     finish()

# Hurdle 2

# while at_goal() != True:
#     finish()

# Hurdle 3

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def finish():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         finish()
#     else:
#         move()

# Hurdle 4

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def finish():
#     turn_left()
#     while wall_on_right():
#         move()

#     turn_right()
#     move()
#     turn_right()
#     while not wall_in_front():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         finish()
#     else:
#         move()

# Maze

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def finish():
#     while not at_goal():
#         if wall_on_right() and wall_in_front():
#             turn_left()
#         elif wall_in_front():
#             turn_right()
#         else:
#             move()

# finish()

# follow along the right path:
