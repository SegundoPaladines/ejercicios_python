#entrada
num = int(input("Ingrese el Limite de Fibonacci: "))

fibo_1 = 0
fibo_2 = 1
fibo = fibo_1 + fibo_2
resultado = f"{fibo_1}, {fibo_2}, {fibo}"

while fibo < num:
    fibo_1 = fibo_2
    fibo_2 = fibo
    fibo = fibo_1 + fibo_2
    
    if fibo < num:
        resultado = f"{resultado}, {fibo}"

print(resultado+"...")