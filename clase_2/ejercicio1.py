#entradas
num_1 = float(input("Ingrese el primer número: "))
num_2 = float(input("Ingrese el segundo número: "))

#proceso
resultado = "El número mayor es:"

if num_1 > num_2:
    resultado = f"{resultado} {num_1}"
else:
    resultado = f"{resultado} {num_2}"

#salida
print(resultado)