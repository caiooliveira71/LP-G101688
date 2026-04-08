import os 

os.system("cls")

def menor(a):
    inflação1 = a * 1.10
    return inflação1


def maior(a):
    inflação2 = a * 1.20
    return inflação2

preco = float(input("digite o preço do produto: "))

inflação1 = menor(preco)
inflação2 = maior(preco)

if preco < 100:
    print(f"VALOR A PAGAR(AUMENTO DE 10%): {inflação1}")
if preco >= 100:
    print(f"VALOR A PAGAR(AUMENTO DE 20%): {inflação2}")