import os 

os.system("cls")

soma = 0
contador = 0
    

while True:
    nota = int(input("digite sua nota: "))
    mais_nota = input("deseja inserir uma nota?\nUse S ou N: ").lower()
    
    soma += nota
    contador += 1
    
    if mais_nota == "n":
       break
      

if contador > 0:
    media = soma / contador
    print(f"numero de notas: {contador}")
    print(f"media aritimedica: {media}")
     
            