def menu(unities):
    i = 1
    for option, amount in unities.items():
        print(f"{i}. {amount} | Opc: {option}")
        i += 1
    return unities


def converter_body():
    print("\n|-----------------------|")
    while True:
        try:
            unity = float(input("\nEnter the amount: "))
            return unity
        except ValueError:
            print("\nPlease enter a valid number.")


def print_result(result):
    print(f"\nResult:\n{result}")
    print("\n|-----------------------|\n")


def meter_cm(amount):
    result = amount * 100
    return f"{amount}m equal to {result}cm"


def kilogram_gm(amount):
    result = amount * 1000
    return f"{amount}kg equal to {result}g"


def liter_ml(amount):
    result = amount * 1000
    return f"{amount}L equal to {result}mL"


def hour_m(amount):
    result = amount * 60
    return f"{amount}h equal to {result}min"


def degrees_f(amount):
    result = amount * (9/5) + 32
    return f"{amount}°C equal to {result}°F"
