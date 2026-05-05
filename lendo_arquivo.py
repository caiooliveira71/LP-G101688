import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Empresa:
    nome: str
    cnpj: str
    telefone: str

    def mostrar_dados(self):
        print(f"nome: {self.nome}")
        print(f"telefone: {self.telefone}")
        print(f"CNPJ: {self.cnpj}\n")
        
lista_empresas = []

with open("Contato_empresas.csv", "r") as arquivo:
    for linha in arquivo:
        nome,cnpj,telefone = linha.strip().split(',')
        lista_empresas.append(Empresa(nome=nome,cnpj=cnpj,telefone=telefone))

for empresa in lista_empresas:
    empresa.mostrar_dados()