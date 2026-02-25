import os

os.system("cls")


maçãs = int(input("digite a quantidade de maçãs: "))

if maçãs < 12:
    print("R$1,30 cada")
    produto = maçãs * 1.30
    
if maçãs >= 12:
    print("R$1,00 cada")
    produto = maçãs * 1
    
print("valor da compra: ", produto)