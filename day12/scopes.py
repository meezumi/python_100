# Modifying Global Scope

enemies = 1 # even if they have the same name,

def increase_enemies():
    enemies = 2 # they are both separate variables 
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies inside function: {enemies}")

# to use the global variable inside the function:

enemies = 1 # even if they have the same name,

def increase_enemies():
    global enemies # now they are the same
    enemies += 1
    print(f"enemies inside function: {enemies}")
    # return enemies + 1 

increase_enemies()
print(f"enemies inside function: {enemies}")

# Global Constants 

PI = 3.14159 # uppercase means its used as a constant 

