import os 
import time 

os.system("cls")

soma = 0
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    nota = int(input("digite sua nota: "))
    soma += nota 
    time.sleep(0.5)

media = soma / QUANTIDADE_NOTAS

print(f"media: {media}")

if media >= 7:
    print("aprovado")
if 4 <= media < 7:
    print("recuperação")
if media < 4:
    print("reprovado")