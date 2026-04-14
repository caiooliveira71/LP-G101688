import os 

os.system("cls")

vetor = []
par = 0
impar = 0
QUANTIDADE = 6

for i in range(QUANTIDADE):
    num = int(input(f"digite o {i} numero: "))
    vetor.append(num)
    
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
        
for c, v in enumerate(vetor, start=1):
    print(f"O numero na posição {c} é {v}!")
    
print(f"quantidade de numeros pares: {par}")
print(f"quantidade de numeros impares: {impar}")
     
