#local and global vars
from debug import score


def greet():
    message = "hello"
    print(message)

greet()
print("hello")
## message is a local variable so it can not be used outside of the function

player_name = "Bob"

def greet2():
    print("Hello", player_name)

greet2()
## player_name is a global function so it can be called in any function inside of the python file

score = 0

def add_points():
    global score    ##global score is calling the global variable to add to it instead of creating a local score
    score = score + 20

add_points()
add_points()

print(scores)