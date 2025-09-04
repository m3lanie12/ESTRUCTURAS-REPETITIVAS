print("SUMA DE PARES E IMPARES")

numero = int(input("Ingresa un número entero: "))

suma_par = 0
suma_impar = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        suma_par += i
    else:
        suma_impar += i

print("Suma de pares:", suma_par)
print("Suma de impares:", suma_impar)
