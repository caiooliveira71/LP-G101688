import os

os.system("cls")

senha_correta = 70650123
login_correto = "caio"

senha = int(input("digite sua senha: "))
login = input("digite seu login: ")
    

for i in range(3):
        if senha == senha_correta and login == login_correto:
            print("bem vindo")
        else:
            print("senha ou login invalido")
            senha = int(input("digite sua senha: "))
            login = input("digite seu login: ")