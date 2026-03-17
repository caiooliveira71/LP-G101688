import os 
import time

os.system("cls")

pares = 0
impares = 0

for i in range(1,5):
    num = int(input("digite um numero: "))
    time.sleep(0.5)
    resultado = num % 2

    if resultado == 0:
        pares += 1 
    else:
        impares += 1

print(f"numero de impares: {impares}")
print(f"numero de pares: {pares}")
