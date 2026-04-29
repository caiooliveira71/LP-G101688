import os 
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    sombrenome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int

# USANDO UMA CLASSE
pessoa1 = Pessoa("Alice","Machado",20)
pessoa2 = Pessoa('Paulo',"Pinto",50)
pet1= Pet('Brutos', 5)
pet2 = Pet('Hades', 3)

print(f"Nome: {pessoa1.nome} {pessoa1.sombrenome}\nIdade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome} {pessoa2.sombrenome}\nIdade: {pessoa2.idade}")
print(f"Nome do pet: {pet1.nome}\nIdade: {pet1.idade}")
print(f"Nome do pet: {pet2.nome}\nIdade: {pet2.idade}")