import random
# numeros
# lower case
# uppercase
# symbols

print("|----------------------|")
print("|--Password Generator--|")
print("|----------------------|")
print("\n")
characters = int(input("# Of characters for your password? (8 or +): "))


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


functions = [create_numero, create_lower_letter,
             create_upper_letter, create_symbol]


def create_password(char_length, functions):
    password = ""
    for character in range(char_length):
        rand_index = random. randint(0, (len(functions) - 1))
        call_function = functions[rand_index]()
        character = call_function
        password += character
    return password


if characters < 8:
    raise ValueError("Password must have 8 or more characters")
else:
    final_password = create_password(characters, functions)
    print(f"Your password is: {final_password}")
