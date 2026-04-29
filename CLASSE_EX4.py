import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    numero: int

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nEmail: {self.email}\nNumero de Telefone: {self.numero}")

print("--DADOS DO CLIENTE--")
cliente = Cliente(
    nome= input("digite seu nome: "),
    email= input("digite seu email: "),
    numero= int(input("digite seu numero de telefone: "))
)
print("--EXIBINDO DADOS DO CLIENTE--")
cliente.mostrar_dados()