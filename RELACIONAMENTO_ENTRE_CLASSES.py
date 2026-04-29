import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereço: 
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    idade: int
    endereço: Endereço

    def mostrando_Cliente(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nEndereço: {self.endereço.logradouro}\nNumero: {self.endereço.numero}")

cliente = Cliente(
    nome= input("Digite seu nome: "),
    idade= int(input("Digite sua idade: ")),
    endereço= Endereço(
        logradouro= input("Digite seu Logradouro: "),
        numero= int(input("Digite seu numero: "))
    )
)
print("--DADOS DO CLIENTE--")
cliente.mostrando_Cliente()