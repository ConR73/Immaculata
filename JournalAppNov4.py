#1 asks the user for a journal entry
#2 saves the entry to a file called "journal.txt" (use append instead of write)
#3 uses try and except so the program prints a friendly message instead of crashing if the file cannot be opened
#4 Has a global counter variable that tracks how many entries have been saved this run, updated inside a function using the global keyword
#5 Prints the counter after each entry

#increases the count stored in a count file that represents the number of journal entries
def increase_count():
    global num_counter
    file = open("journal_counter.txt","r")
    counter = file.read()
    if counter == "":
        num_counter = 1
    else:
        try:
            num_counter = int(counter)+1
        except ValueError:
            print("bad")
    file.close()
    file = open("journal_counter.txt","w")
    file.write(str(num_counter))
    file.close()


#amends the new entry to the journal file with addition of the entry number provided by the counter variable
# from the counter folder
def add_entry():
    try:
        increase_count()
        file = open("journal_counter.txt","r")
        num = file.read()
        file.close()
        message = input("Today's journal entry: ")
        file = open("journal.txt","a")
        file.write(f"Journal Entry : {num} | {message}\n")
    except FileNotFoundError:
        print("error | file not found")

# starts the entry adding and prints the file contents and loops the function when the user responds with "yes"
def journal_loop():
    add_entry()
    file = open("journal.txt","r")
    contents = file.read()
    file.close()
    print(contents)
    response = input("Add another entry? : yes/no ")
    try:
        if response == "yes":
            journal_loop()
        elif response == "no":
            print("Thanks have a good day")
    except ValueError:
        print("wrong input")

#calls the looping for the first time
journal_loop()
