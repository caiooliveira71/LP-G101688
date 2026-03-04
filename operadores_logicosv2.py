import os 

os.system("cls")

usuario = "estevamvaleria9@gmail.com"
senha_cadastrada = "70650123"

login = str(input("digite seu e-mail: "))
senha = str(input("digite sua senha: "))

if login == usuario and senha == senha_cadastrada:
    print("BEM-VINDO")
else:
    print("ACESSO NEGADO")