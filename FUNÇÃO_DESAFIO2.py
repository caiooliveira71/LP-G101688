import os

os.system("cls")

QUANTIDADE = 5
numeros = []
# Variáveis para armazenar os números
for i in range(QUANTIDADE):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = num
menor_numero = num
soma_impares = 0
soma_pares = 0
soma_geral = 0

# Processando cada número
for num in numeros:
    if num % 2 == 0:
        quantidade_pares += 1
        soma_pares += num
    else:
        quantidade_impares += 1
        soma_impares += num

    if num > 0:
        quantidade_positivos += 1
    if num < 0:
        quantidade_negativos += 1

    maior_numero = max(maior_numero, num)
    menor_numero = min(menor_numero, num)
    
    soma_geral += num

def media(a):
    if QUANTIDADE > 0:
        return soma_geral / QUANTIDADE
    else:
        return 0
        

def media_pares(a):
        if quantidade_pares > 0:
            return soma_pares / quantidade_pares
        else:
            return 0
    

def media_impares(a):
        if quantidade_impares > 0:
            return soma_impares / quantidade_impares
        else:
            return 0
        
numeros.sort(reverse = True
media_geral = media(num)
media_pares = media_pares(num)
media_impares = media_impares(num)

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior numero: {maior_numero}")
print(f"Menor numero: {menor_numero}")
print(f"Media dos pares: {media_pares}")
print(f"Media dos impares: {media_impares}")
print(f"Media Geral: {media_geral}")
print(numeoros)
