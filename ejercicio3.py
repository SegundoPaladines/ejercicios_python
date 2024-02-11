#Mensaje de inicio
print("Inicio app ... \n")

for i in range(4):
    a = i + 1
    for j in range(4):
        b = j + 2
        for k in range(4):
            c = k + 3
            for l in range(4):
                d = l + 4
                for m in range(4):
                    e = m + 5
                    try:
                        y = (1-(c/a))/((e/d)-(b/a))
                        x = (c-b*y)/(a)
                        print(f"Valor de x: {x}, valor de y: {y}")
                    except Exception as e:
                        pass

