print("PIRAMIDE DE ASTERISCOS")

asterisco = int(input("Ingresa la altura de la pirámide: "))

for i in range(1, asterisco + 1):
    print(" " * (asterisco - i), end="")
    print("*" * (2 * i - 1))
