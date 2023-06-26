# sumas, restas, divisiones, multiplicaciones

# método #1
operador = input("OPERADOR: (+,-,*,/) ")
numero_1 = float(input("Número 1: "))
numero_2 = float(input("Número 2: "))

if operador == "+":
    resultado = numero_1 + numero_2
elif operador == "-":
    resultado = numero_1 - numero_2
elif operador == "*":
    resultado = numero_1 * numero_2
elif operador == "/":
    resultado = numero_1 / numero_2
else:
    print("Operador no válido")

print(resultado)

# método #2
# operador = input("OPERADOR: (+,-,*,/) ")
# numero_1 = input("Número 1: ")
# numero_2 = input("Número 2: ")

# resultado = numero_1 + operador + numero_2

# r_final = eval(resultado)

# print(r_final)
