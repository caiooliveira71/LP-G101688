import os

os.system("cls")

soma = 0
QUANTIDADE = 2

for i in range(QUANTIDADE):
    while True:
        nota = int(input("digite sua nota: "))
        
                
        if nota < 0  or nota > 10:
            print("nota invalida")
            print("...tente novamente")
        else:
            soma += nota
            break
    
media = soma / QUANTIDADE
print("nota valida")
print(f"sua media é: {media}")