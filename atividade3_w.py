import os 

os.system("cls")

senha_correta = 70650123
login_correta = "caio"

while True:
    senha = int(input("digite sua senha: "))
    login = input("digite seu login: ")
    
    if senha == senha_correta and login == login_correta:
        print("senha e login valido")
        print("bem vindo")
        break
    else:
        print("senha ou login invalido")
    

    