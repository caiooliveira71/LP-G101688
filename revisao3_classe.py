import os 
from dataclasses import dataclass

os.system("cls")

lista_funcionarios = []

@dataclass
class Funcionario:
    nome: str
    email: str
    telefone: int

    def mostrar_dados(self):
        print("\n ---Dados do funcionario---")
        print(f"nome: {self.nome}")
        print(f"email: {self.email}")
        print(f"telefone: {self.telefone}")

while True:
    print("\nSolicitando dados do funcionario")
    novo_funcionario = Funcionario(
        nome=input(f"Digite o nome do funcionario: "),
        email=input(f"Digite o email do funcionario: "),
        telefone=int(input(f"Digite o telefone do funcionario: "))
    )
    lista_funcionarios.append(novo_funcionario)
    continuar = input("deseja continuar o cadastro de funcionarios?\ndigite S ou N:").lower()
    
    if continuar == "n":
        break

with open("dados_funcionarios.txt", "a") as arquivo_funcionarios:
    for funcionario in lista_funcionarios:
        arquivo_funcionarios.write(f'{funcionario.nome}, {funcionario.email}, {funcionario.telefone}\n')
        

for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()