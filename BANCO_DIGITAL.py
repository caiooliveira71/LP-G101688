import os 

os.system("cls")

banco = []
    
def logo():
    print("         -------------------")
    print("             BANCO SEXY")
    print("         -------------------")


def criar_usuario():
    nome_usuario = input("Digite o seu nome de usuario: ")
    senha = input("digite a senha da sua conta: ")


def depositar():
    depositar = int(input("digite o quanto deseja depositar: "))
    banco.append(depositar)
    

def sacar():
    valor = int(input("Digite o valor que deseja sacar: "))
    saldo_atual = sum(banco)

    if valor > saldo_atual:
        print("SALDO INSUFICIENTE!")
    else: 
        banco.clear()
        banco.append(saldo_atual-valor)
        print("SAQUE REALIZADO!")


def saldo():
    print("Saldo Bancario:",sum(banco))


while True:
    logo()
    print("""           ------MENU------
            1-CRIAR USUARIO
            2-DEPOSITAR
            3-SACAR
            4-SALDO
            5-SAIR""")
    opção = int(input("Digite a opção desejada: "))

    match opção:
        case 1:
            criar_usuario()
        case 2:
            depositar()
        case 3:
            sacar()
        case 4:
            saldo()
        case 5:
            print("OBRIGADO POR USAR O BANCO SEXY")
            break
        case _:
            print("OPÇÃO NÃO ENCONTRADA!")
            print("TENTE NOVAMENTE!")
        