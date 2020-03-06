from threading import Thread
import time
inicio = time.time()

def fib(n):
    soma = 1
    f0 = 1
    f1 = 1
    for x in range(0, n):
        soma = f0 + f1
        f0 = f1
        f1 = soma
    return soma

for y in range(-1, 800000):
    #numero = fib(y)
    #print(numero)
    fibonacci = Thread(target=fib, args=[y])

fim = time.time()
print(fim - inicio)

