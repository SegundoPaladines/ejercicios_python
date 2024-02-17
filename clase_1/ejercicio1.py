#Mensaje de inicio
print("Inicio app ... \n")

#Entradas
#Datos de la base
length_b = float(input("Ingrese el valor del length_b: "))
width_b = float(input("Ingrese un valor del width_b: "))
altitude_b = float(input("Ingrese un valor del altitude_b: "))

#datos de la puerta
width_p = float(input("Ingrese un valor del width_p: "))
altitude_p = float(input("Ingrese un valor del altitude_p: "))

#proceso
a_base = length_b * width_b
volumen = a_base*altitude_b

pared_1 = length_b * altitude_b
pared_2 = width_b * altitude_b

a_puerta = width_p * altitude_p

#salidas
print(f"Area de la base {a_base}")
print(f"Area de volumen {volumen}")
print(f"Area de pared 1 {pared_1}")
print(f"Area de pared 2 {pared_2}")
print(f"Area de puerta {a_puerta}")