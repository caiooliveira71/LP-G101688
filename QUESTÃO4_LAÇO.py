import time

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))
num4 = int(input("Digite um numero: "))
num5 = int(input("Digite um numero: "))

soma = num1 + num2 + num3 + num4 + num5

for i in range(1,soma):
    print(i)
    time.sleep(0.05)