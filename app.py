import string
import random

letter_input1 = input("Enter \"v\" for vowels, \"c\" for consonents or \"l\" for letters")
letter_input2 = input("Enter \"v\" for vowels, \"c\" for consonents or \"l\" for letters")
letter_input3 = input("Enter \"v\" for vowels, \"c\" for consonents or \"l\" for letters")
letter_input4 = input("Enter \"v\" for vowels, \"c\" for consonents or \"l\" for letters")
letter_input5 = input("Enter \"v\" for vowels, \"c\" for consonents or \"l\" for letters")

vowels = 'aeiouy'
consonents = 'bcdfghjklmnopqrstwxz'
letters = string.ascii_lowercase


def generator():
    if letter_input1 == "v":
        letter1 = random.choice(vowels)
    elif letter_input1 == "c":
        letter1 = random.choice(consonents)
    elif letter_input1 == "l":
        letter1 = random.choice(letters)
    else:
        letter1 = letter_input1

    if letter_input2 == "v":
        letter2 = random.choice(vowels)
    elif letter_input2 == "c":
        letter2 = random.choice(consonents)
    elif letter_input2 == "l":
        letter2 = random.choice(letters)
    else:
        letter2 = letter_input2

    if letter_input3 == "v":
        letter3 = random.choice(vowels)
    elif letter_input3 == "c":
        letter3 = random.choice(consonents)
    elif letter_input3 == "l":
        letter3 = random.choice(letters)
    else:
        letter3 = letter_input3

    if letter_input4 == "v":
        letter4 = random.choice(vowels)
    elif letter_input4 == "c":
        letter4 = random.choice(consonents)
    elif letter_input4 == "l":
        letter4 = random.choice(letters)
    else:
        letter4 = letter_input4

    if letter_input5 == "v":
        letter5 = random.choice(vowels)
    elif letter_input5 == "c":
        letter5 = random.choice(consonents)
    elif letter_input5 == "l":
        letter5 = random.choice(letters)
    else:
        letter5 = letter_input5

    name = letter1 + letter2 + letter3 + letter4 + letter5

    return name


for babyname in range(20):
    print("Your baby's new name can be: " + generator())
