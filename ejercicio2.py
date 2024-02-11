import math

#Mensaje de inicio
print("Inicio app ... \n")

#Entradas
x_1 = float(input("Ingrese la coordenada X_1: "))
y_1 = float(input("Ingrese la coordenada Y_1: "))

x_2 = float(input("Ingrese la coordenada X_2: "))
y_2 = float(input("Ingrese la coordenada y_2: "))

#proceso
d = math.sqrt(((x_2-x_1)**2)+((y_2-y_1)**2))

#salida
print(f"Distancia entre los dos puntos: {d}")