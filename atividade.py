import os

os.system("cls")

while True:
    idade = int(input("digite sua idade: "))
    if idade < 18:
        print("ACESSO NEGADO")
        print("TENTE NOVAMENTE")
    else:
        print("ACESSO PERMITIDO")
        break

print("---FIM---")