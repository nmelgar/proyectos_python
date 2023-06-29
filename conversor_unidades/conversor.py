from unidades import unities
from funciones import *

run = True
print("\n|-----------------------|")
print("|----Unit Converter-----|")
print("|-----------------------|")

while run:
    print("\n")
    menu(unities)
    print("\nType E to exit")
    user_choice = input("\nChoose an option: ")

    if user_choice.lower() == "m":
        unity = converter_body()
        result = meter_cm(unity)
        print_result(result)

    elif user_choice.lower() == "kg":
        unity = converter_body()
        result = kilogram_gm(unity)
        print_result(result)

    elif user_choice.lower() == "l":
        unity = converter_body()
        result = liter_ml(unity)
        print_result(result)

    elif user_choice.lower() == "h":
        unity = converter_body()
        result = hour_m(unity)
        print_result(result)

    elif user_choice.lower() == "c":
        unity = converter_body()
        result = degrees_f(unity)
        print_result(result)

    elif user_choice.lower() == "e":
        print("\n|-----------------------|")
        print("|---Come back later-----|")
        print("|-----------------------|")
        print("\n")
        run = False
    else:
        print("\nPrint enter a valid option.")
