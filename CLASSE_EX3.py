import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    numero: int

print("--DADOS DO CLIENTE--")
cliente = Cliente(
    nome= input("digite seu nome: "),
    email= input("digite seu email: "),
    numero= int(input("digite seu numero de telefone: "))
)
print("--EXIBINDO DADOS DO CLIENTE--")
print(f"Nome: {cliente.nome}\nEmail: {cliente.email}\nNumero de Telefone: {cliente.numero}")