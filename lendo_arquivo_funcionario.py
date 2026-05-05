import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Funcionarios:
    nome: str
    idade: int

    def mostrar_dados(self):
        print(f"nome: {self.nome}")
        print(f"idade: {self.idade}\n")
        
lista_funcionarios = []

with open("funcionarios.csv", "r") as arquivo:
    for linha in arquivo:
        nome,idade = linha.strip().split(',')
        lista_funcionarios.append(Funcionarios(nome=nome,idade=idade))

for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()