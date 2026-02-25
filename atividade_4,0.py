import os

os.system("cls")


num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))

media = (num1 + num2) / 2
soma = num1 + num2 
produto = num1 * num2

if num1 > num2:
    print("num1 é maior")
    print("num2 é menor")
if num1 < num2:
    print("num1 é menor")
    print("num2 é menor")


if num1 == num2:
    print("são iguais")
else: 
    print("não são iguais")
    

print(f"media: {media}")
print(f"soma: {soma}")
print(f"produto: {produto}")

