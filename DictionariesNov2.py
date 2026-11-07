#Dictionaries
from multiprocessing import resource_sharer

my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"
my_dictionary["hei"] = "hello"
my_dictionary["kiitos"] = "thank you"
my_dictionary["ole hyva"] = "please / you're welcome"
my_dictionary["kylla"] = "yes"
my_dictionary["ei"] = "no"
my_dictionary["anteeksi"] = "sorry / excuse me"
my_dictionary["moi"] = "Hi / Bye"
my_dictionary["ystava"] = "friend"
my_dictionary["perhe"] = "family"

#prints out the length of the dictionary (number of words)
print(len(my_dictionary))
#prints out the total dictionary
print(my_dictionary)
#prints specified word's translation
print(my_dictionary["apina"])

#asks for a word in Finnish and gives the English Translation
# if word is not in the dictionary it prints "not found"
word = input("input word")
if word in my_dictionary:
    print("Translation", my_dictionary[word])
else:
    print("word not found")

#creates dictionary with integers
results = {}
results["Mary"]=4
results["Alice"]=5
results["Tim"]=2

print(results)

#creates dictionary of lists
lists = {}
lists[5]=[1,2,3]
lists[20]=[2,4,5,7,1]
lists[3]=[3,2,1]
print(lists)

#amending dictionary values and overwriting
my_dictionary["suuri"]="big"
my_dictionary["suuri"]="large"
##can overwrite dictionary values

#list of words from chapter 1 of 1984 (I'm currently reading this)
word_list = ("It", "was", "a", "bright", "cold", "day", "in", "April", "and", "the", "clocks", "were",
             "striking", "thirteen", "Winston", "Smith", "his", "chin", "nuzzled", "into", "his", "breast",
             "in", "an", "effort", "to", "escape", "the", "vile", "wind", "slipped", "quickly", "through",
             "the", "glass", "doors", "of", "Victory", "Mansions", "though", "not", "quickly", "enough",
             "to", "prevent", "a", "swirl", "of", "gritty", "dust", "from", "entering", "along", "with",
             "him", "The", "hallway", "smelt", "of", "boiled", "cabbage", "and", "old", "rag", "mats", "At",
             "one", "end", "of", "it", "a", "coloured", "poster", "too", "large", "for", "indoor", "display",
             "had", "been", "tacked", "to", "the", "wall", "It", "depicted", "simply", "an", "enormous",
             "face", "more", "than", "a", "metre", "wide", "the", "face", "of", "a", "man", "of", "about",
             "forty-five", "with", "a", "heavy", "black", "moustache", "and", "ruggedly", "handsome",
             "features", "Winston", "made", "for", "the", "stairs")

#counts the number of times each word is used
def counts(my_list):
    words={}
    for word in my_list:
        if word not in words:
            words[word] = 0
        words[word]+= 1
    return words

#prints a word found in the list with the number of times it appears next to it
print(counts(word_list))