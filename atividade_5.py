import os

os.system("cls")


idade = int(input("digite sua idade: "))

if idade < 16:
    print("não podem votar")
if 16 <= idade <= 17:
    print("voto opcional")
if 18 <= idade < 65 :
    print("voto obrigatorio")
if idade >= 65:
    print("não é obrigado")
