import os 

os.system("cls")

nota = int(input("digite sua nota: "))

while nota < 0 or nota > 10:
    print(f"nota invalida") 
    
    break

print(f"nota validada")
    
    