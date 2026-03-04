import os

os.system("cls")

nome = input("digite seu nome: ")
media = int(input("digite sua media: "))
numero_de_faltas = int(input("digite seu numero de faltas: "))

if media >= 7 and numero_de_faltas <= 40:
    print("APROVADO")
else:
    print("REPROVADO")