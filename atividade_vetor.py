import os 

os.system("cls")

vetor_notas = []
QUANTIDADE_NOTA = 4

for i in range(QUANTIDADE_NOTA):
    nota = int(input(f"digite sua {i+1}°: "))
    vetor_notas.append(nota)
    
media = sum(vetor_notas) / QUANTIDADE_NOTA

for i, uma_nota in enumerate(vetor_notas, start=1):
    print(f"{i}° nota: {uma_nota}")
    
print(f"media: {media}")

if media >= 7:
    print("aprovado")
if media >= 5 and media < 7:
    print("recuperação")
if media < 5:
    print("reprovado")