file = open("scores.txt", "w")
file.write("Player One: 100pt\n")
file.write("Player Two: 150pt\n")
file.close()

file = open("scores.txt", "a")
file.write("Player Three: 80pt\n")
file.close()

file = open("scores.txt","r")
contents = file.read()
print(contents)
file.close()

with open("scores.txt","a") as file:
    file.write("Player Four: 240pt\n")