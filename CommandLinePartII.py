directory = ["apple", "banana", "orange",
 "grape", "mango", "peach", "cherry", "lemon", "watermelon", "strawberry", "computer", "keyboard", "mouse", "monitor", "laptop", "phone",
 "internet", "software", "programming", "python", "school", "teacher", "student", "classroom", "book", "pencil",
"notebook","library","science", "mathematics","happy","beautiful", "creative","adventure","friendship"]


def Search(directory):
    word = input("Type the word you want to search for: ")
    found = False

    for i in range(len(directory)):
        if directory[i] == word:
            print("Found", word, "at index", i, "in directory")
            found = True

    if not found:
        print(word, "Not found")

Search(directory)
