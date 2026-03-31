import os 

os.system("cls")

numeros = []
negativo = 0
soma_positivos = 0
QUANTIDADE = 5

for i in range(QUANTIDADE):
    num = int(input("digite um numero: "))
    
    if num < 0:
        negativo += 1
    if num > 0:
        soma_positivos += num
        
for c, v in enumerate(numeros, start=1):
    print(f"Na posição {c} o numero é {v}!")
    
print(f"numeros de negativos: {negativo}")
print(f"soma dos numeros positivos: {soma_positivos}")