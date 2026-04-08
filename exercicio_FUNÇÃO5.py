import os 

os.system("cls")

soma = 0
def media(nota):
    soma = 0
    for nota in numero:
        soma += nota
    return soma / 3


numero = []

for i in range(3):
    nota = int(input("digite uma nota: "))
    numero.append(nota)


media = media(numero)

print(f"media: {media}")