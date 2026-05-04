import os 
from dataclasses import dataclass

os.system("cls")

lista_clientes = []

@dataclass
class Cliente: 
    nome: str
    idade: int
    peso: float
    altura: float
    
    def mostrar_dados(self):
        print("\n Dados do cliente")
        print(f"nome: {self.nome}")
        print(f"idade: {self.idade}")
        print(f"peso: {self.peso}KG")
        print(f"altura: {self.altura}cm")

print("Solicitando dados")
for i in range(2):
    novo_cliente = Cliente(
        nome=input("digite o nome: "),
        idade=int(input("digite a idade: ")),
        peso=float(input("digite o peso: ")),
        altura=float(input("digite a altura: "))
    )
    lista_clientes.append(novo_cliente)

for cliente in lista_clientes:
    cliente.mostrar_dados()