import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Cliente:
    nome: str
    email: str
    numero: int

@dataclass
class Funcionario:
    nome: str
    matricula: int
    email: str
    setor: str

cliente1 = Cliente('Maria',"maria@gmail.com", 93457895)
funcionario1 = Funcionario("João",73737,"joão@gmail.com","Industrial")

print("--DADOS DOS CLIENTE--")
print(f"Nome: {cliente1.nome}\nEmail: {cliente1.email}\n Numero de Telefone: {cliente1.numero}")

print("--DADOS DO CLT--")
print(f"Nome do funcionario: {funcionario1.nome}\nMatricula: {funcionario1.matricula}\nEmail: {funcionario1.email}\nSetor: {funcionario1.setor}")