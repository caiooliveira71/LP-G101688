import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereço: str

    def mostrar_dados(self):
        print(f"Nome: {pessoa.nome}\nEmail: {pessoa.email}\nTelefone: {pessoa.telefone}\nEndereço: {pessoa.endereço}")

pessoa = Pessoa(
    nome = input("digite seu nome: "),
    email= input("digite seu email: "),
    telefone= int(input("digite seu telefone: ")),
    endereço= input("digite seu endereço: ")
)

print("--DADOS DO CLIENTE--")
pessoa.mostrar_dados()