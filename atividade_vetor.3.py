import os 

os.system("cls")

vetor = []
QUANTIDADE = 6
pares = 0
impares = 0

for i in range(QUANTIDADE):
    num = int(input(f"{i+1}° numero: "))
    vetor.append(num)
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
   
    
for i, num in enumerate(vetor, start=1):
    print(f"numero {i}°: {num}")
   
print(f"numeros impares: {impares}")
print(f"numeros pares: {pares}")