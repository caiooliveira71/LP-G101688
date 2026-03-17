import os
import time

os.system("cls")

num = int(input("digite um numero: "))

for i in range(1,10):
    resultado = num * i
    print("{} X {} = {}".format(num, i, resultado))
    time.sleep(2)