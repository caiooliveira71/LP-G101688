import os
import time

os.system("cls")

soma = 0

for i in range(1,6,1):
    num = int(input("digite um numero: "))
    soma += num
    time.sleep(0.5)

print(f"soma: {soma}")