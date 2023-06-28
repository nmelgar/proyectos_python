from funciones import *

unities = {"m": "m->cm", "kg": "kg->g", "l": "L->mL", "h": "h->min", "c": "°C->°F", "m2": "m2->ft2",
           "kmh": "km/h->m/s", "t": "t->kg", "l100": "L/100km->gal/mi", "usd": "USD->Euro"}

run = True
print("|-----------------------|")
print("|----Unit Converter-----|")
print("|-----------------------|")
print("\n")


while run:
    print("\n")
    menu(unities)
    print("\nType E to exit")
    user_choice = input("\nChoose an option: ")

    if user_choice.lower() == "m":
        unity = converter_body()
        result = meter_cm(unity)

    elif user_choice.lower() == "kg":
        unity = converter_body()
        result = kilogram_gm(unity)

    elif user_choice.lower() == "l":
        unity = converter_body()
        result = liter_ml(unity)

    elif user_choice.lower() == "h":
        unity = converter_body()
        result = hour_m(unity)

    print(f"\nResult:\n{result}")
    print("\n|-----------------------|\n")
