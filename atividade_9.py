import os

os.system("cls")

matricula_empresario = int(input("digite sua matricula: "))
ano_nascimento = int(input("digite seu ano de nascimento: "))
tempo_trabalho = int(input("digite seu tempo de trabalho: "))

idade = 2026 - ano_nascimento

print(f"idade: {idade}")
print(f"tempo de trabalho: {tempo_trabalho}")
print(f"codigo do empregado: {matricula_empresario}")

if idade >= 65 or tempo_trabalho >= 30:
    print("requeri aposentadoria")
else: 
    print("não requerer")


