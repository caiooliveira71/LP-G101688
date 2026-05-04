import os 
from dataclasses import dataclass

os.system("cls")

lista_pets = []

@dataclass
class Pets:
    nome: str
    idade: int
    raça: str

    def mostrar_dados(self):
        print("\n ---Dados do Pet---")
        print(f"nome do Pet: {self.nome}")
        print(f"idade do Pet: {self.idade}")
        print(f"raça: {self.raça}")

while True:
    print("\nSolicitando dados do Pet")
    for i in range(2):
        novo_pet = Pets(
            nome=input("Digite o nome do Pets: "),
            idade=input("Digite a idade do Pet: "),
            raça=input("Digite a raça do Pet: ")
        )
        lista_pets.append(novo_pet)
    continuar = input("deseja continuar o cadastro dos seus pets?\ndigite S ou N:").lower()
    
    if continuar == "n":
        break

for pet in lista_pets:
    pet.mostrar_dados()