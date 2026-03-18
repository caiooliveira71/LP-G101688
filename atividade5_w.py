import os 

os.system("cls")

soma = 0
for i in range(3):
    while True:
        nota = int(input("digite sua nota: "))
        
        if nota < 0 or nota > 10:
            print("nota invalida")
            print("...tente novamente")
        else:
            soma += nota
            break

media = soma / 3
print(f"sua media é: {media}")
print("nota valida")


if media >= 7:
    print("aprovado") 
if 5 <= media < 6.9:
    print("recuperação")
if media < 5:
    print("reprovado")