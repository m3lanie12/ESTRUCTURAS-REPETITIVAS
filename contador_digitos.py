print("CONTADOR DE DIGITOS")

numero = int(input("Ingresa un numero: "))

if numero == 0:
    dig = 1
else:
    dig = 0
    while numero > 0:
        numero = numero // 10   
        dig += 1      

print("El numero tiene", dig , "digitos.")


