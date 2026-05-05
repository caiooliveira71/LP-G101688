import os 
from dataclasses import dataclass

os.system("cls")

lista_empresas = []

@dataclass
class Empresa:
    nome: str
    cnpj: str
    telefone: str
    
    def mostrar_dados(self):
        print("---Dados da empresa---\n")
        print(f"nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"CNPJ: {self.cnpj}\n")


    print("---Solicitando dados---")
nova_empresa = Empresa(
    nome=input("Digite o nome da empresa: "),
    cnpj=input("Digite o CNPJ da empresa:"),
    telefone=input("Digite o telefone da empresa: ")
    )
lista_empresas.append(nova_empresa)

for empresa in lista_empresas:
    empresa.mostrar_dados()

with open("Contato_empresas.csv", "a", encoding="utf-8") as arquivo:
    for empresa in lista_empresas:
        arquivo.write(f"{empresa.nome},{empresa.cnpj},{empresa.telefone}\n")
        print("Dados salvos com sucesso!")
    