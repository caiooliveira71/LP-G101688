import os 
import time

os.system("cls")

soma = 0
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("digite sua nota: "))
    soma += nota 
media = soma / QUANTIDADE_NOTAS
print(f"media: {media}")
