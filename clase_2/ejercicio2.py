#Entradas
num = int(input("Ingrese un número entero: "))

#proceso
i = 1
counter = 0
while i <= num:
    if num % i == 0:
        counter = counter + 1
    
    i = i + 1

#salida
if counter > 2:
    print("El numero ingresado NO es primo")
else:
    print("El numero ingresado es primo")