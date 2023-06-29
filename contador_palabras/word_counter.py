texto = "hola hola"


def char_counter(text):
    counter = 0
    for _ in text:
        counter += 1
    return counter


def word_counter(text):
    words = 0
    split = text.split()
    for _ in split:
        words += 1
    return words


# result = char_counter(texto)
# print(f"hay {result} caracteres")

result = word_counter(texto)
print(f"hay {result} palabras")
