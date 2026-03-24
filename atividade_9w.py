import os 

os.system("cls")

soma = 0
soma_pares = 0
contador = 0
pares = 0
impar = 0

while True:
    nota = int(input("digitem sua nota: "))
    
    if nota == 0:
        break
    
    soma += nota
    contador += 1
    
    if nota % 2 == 0:
        pares += 1
        soma_pares += nota
    else:
        impar += 1


print(f"quatidade de numeros pares: {pares}")
print(f"quatidade de numeros impares: {impar}")

if pares > 0:
    media_pares = soma_pares / pares

print(f"media dos numeros pares: {media_pares}")

    
if contador > 0:  
    media_geral = soma / contador
    print(f"media geral: {media_geral}")

    