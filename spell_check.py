#code used to test Github
#test2


import csv
import string

dict_words = []
sugg = []


def load_dict():
    global dict_words
    f = open("dictionary.csv", "r")
    reader = csv.reader(f)
    dict = list(reader)
    for i in dict:
        dict_words.append(i[0])
    dict_words.pop(0)

# 1. Check a dictionary to determine if word is correctly spelled.
# 2. If not, call a set of functions that generate "near by, correctly spelled words."
#  3. Return suggested corrections.
def check_word(word):
    global dict_words
    global sugg
    if word in dict_words:
        u = True
    else:
        transpose_let(word)
        insert_let(word)
        insert_space(word)
        remove_let(word)

        u = sugg
    return u

def transpose_let(word):
    global dict_words
    global sugg

    for i in range(0, len(word) - 1):
        word2 = word[:i] + word[i + 1] + word[i] + word[i + 2:]
        if word2 in dict_words:
            sugg.append(word2)
    return sugg

def insert_let(word):
    global dict_words
    global sugg
    a = list(string.ascii_lowercase)

    for i in range(0, len(word) + 1):
        for j in range(0, len(a)):
            word2 = word[:i] + a[j] + word[i:]
            if word2 in dict_words:
                sugg.append(word2)
    return sugg

def insert_space(word):
    global dict_words
    global sugg
    for i in range(1, len(word)):
        word2 = word[:i]
        word3 = word[i:]
        if word2 in dict_words and word3 in dict_words:
            sugg.append(word2 + " " + word3)
    return sugg

def remove_let(word):
    global sugg
    global dict_words
    for i in range(0, len(word) - 1):
        word2 = word.replace(word[i+1], "")
        if word2 in dict_words:
            sugg.append(word2)
    return sugg

def append_to_dictionary(r):
    print("In writer.")
    f = open("dictionary.csv","a")
    csv_writing = csv.writer(f)
    csv_writing.writerow(r)
    f.close()

def update_corrections(old_word, new_word):
    global dict_words
    if old_word in dict_words:
        with open('dictionary.csv', 'a') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow([old_word, 0, 0, 1, 0])

    else:
        with open('dictionary.csv', 'a') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow([new_word, 0, 0,  1, 0])


    return
