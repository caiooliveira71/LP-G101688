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

for i in range(3):
    print("\nSolicitando dados do funcionario")
    novo_funcionario = Funcionario(
        nome=input(f"Digite o nome do {i+1}° funcionario: "),
        email=input(f"Digite o email do {i+1}° funcionario: "),
        telefone=int(input(f"Digite o telefone do {i+1}° funcionario: "))
    )
    lista_funcionarios.append(novo_funcionario)

for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()