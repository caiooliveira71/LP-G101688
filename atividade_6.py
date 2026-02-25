import os

os.system("cls")


num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))

if num1 < num2: 
     print("numero 2 é maior")
     print("numero 1 é menor")
if num1 > num2:
     print("numero 2 é menor")
     print("numero 1 é maior")
     
     
print(f"primeiro numero: {num1}")
print(f"segundo numero: {num2}")