import os 

os.system("cls")

vetor = []
QUANTIDADE = 2
maior = 0
menor = 0
contador = 0

for i in range(QUANTIDADE):
    num = int(input(f"{i+1}° numero: "))
    vetor.append(num)
    contador += 1
    
for i, um_num in enumerate(vetor, start=1):
    print(f"numero {i}°: {um_num}")
    
maior = max(vetor)
menor = min(vetor)
    
print(f"maior numero: {maior}")
print(f"menor numero: {menor}")