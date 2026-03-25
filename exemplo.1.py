import os 

os.system("cls")

vetor_notas = []

for i in range(3):
    nota = float(input("digite uma nota: "))
    vetor_notas.append(nota)
    
for i in range(3):
    print(f"nota: {vetor_notas[i]}")