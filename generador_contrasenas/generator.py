import random
# numeros
# lower case
# uppercase
# symbols

# characters = int(input("How many characters? (8 or +)"))


def create_numero():
    # return random number between 0 - 9 (both included)
    return str(random. randint(0, 9))


def create_lower_letter():
    letters = "abcdefghijklmnopqrstuvwxyz"
    i = random. randint(0, (len(letters) - 1))
    return letters[i]


def create_upper_letter():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = random. randint(0, (len(letters) - 1))
    return letters[i]


def create_symbol():
    symbols = '!"#$%&/()=?][_:;,./*-+]'
    i = random. randint(0, (len(symbols)-1))
    return symbols[i]


functions = [create_numero(), create_lower_letter(),
             create_upper_letter(), create_symbol()]


def create_password(char_length, functions):
    password = ""
    counter = 0
    while counter < char_length:
        caracter = ""
        rand_index = random. randint(0, (len(functions) - 1))
        add_character = functions[rand_index]
        caracter = add_character
        password += caracter
        counter += 1

    return password


print(create_password(12, functions))
