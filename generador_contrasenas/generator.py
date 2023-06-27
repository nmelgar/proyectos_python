import random
# numeros
# lower case
# uppercase
# symbols

# characters = int(input("How many characters? (8 or +)"))

def create_numero():
    # return random number between 0 - 9 (both included)
    print(random. randint(0, 9))

def create_lower_letter():
    letters = "abcdefghijklmnopqrstuvwxyz"
    i = random. randint(0, (len(letters)))
    return letters[i]

def create_upper_letter():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = random. randint(0, (len(letters)))
    return letters[i]

def create_symbol():
    symbols = '!"#$%&/()=?][_:;,./*-+]'
    i = random. randint(0, (len(symbols)))
    return symbols[i]

print(create_symbol())