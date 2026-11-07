try:
    age = int(input("Enter your age: "))
    print("You are", age, "years old.")
except ValueError:
    print("Please enter a integer for your age, not words.")

try:
    with open("scores.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("That file is not found")