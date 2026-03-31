import os 

os.system("cls")

vetor = []
QUANTIDADE = 5

for i in range(QUANTIDADE):
    num = int(input("digite um numero: "))
    
    if num < 0:
        num = 0
    
    vetor.append(num)
    
for c, v in enumerate(vetor, start=1):
    print(f"Na posição {c} o numero é {v}!")
    