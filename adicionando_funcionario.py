import os 
from dataclasses import dataclass

os.system("cls")

QUANTIDADE_FUNCIONARIOS = 3
lista_funcionarios = []

@dataclass
class Funcionarios:
    nome: str
    idade: int


    def mostrar_dados(self):
        print(f"nome: {self.nome}")
        print(f"Idade: {self.idade}\n")


print("---Solicitando dados---")
for i in range(QUANTIDADE_FUNCIONARIOS):
    novo_funcionario = Funcionarios(
        nome=input("Digite o nome do funcionario: "),
        idade=int(input("Digite a idade do funcionario: "))
    )
    lista_funcionarios.append(novo_funcionario)


print("---Exibindo dados---")
for funcionario in lista_funcionarios:
    funcionario.mostrar_dados()

print("---Salvando dados---")
with open("funcionarios.csv", "a", encoding="utf-8") as arquivo:
    # for it
    for funcionario in lista_funcionarios:
        arquivo.write(f"{funcionario.nome},{funcionario.idade}\n")
    print("Dados salvos com sucesso!")