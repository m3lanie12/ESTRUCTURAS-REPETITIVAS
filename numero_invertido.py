print("NUMERO INVERTIDO")

num = int(input("Ingresa un número entero: "))

inv = 0

while num > 0:
    digito = num % 10
    inv = inv * 10 + digito
    num //= 10

print("Número invertido:", inv)

