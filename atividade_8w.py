import os 

os.system("cls")

soma = 0
contador = 0

while True:
    nota = int(input("digite sua nota: "))
    
    if nota < 0:
        break
    
    soma += nota
    contador += 1
  

if contador > 0:
    media = soma / contador
    print(f"media: {media}")
else:
    print("nota invalida")