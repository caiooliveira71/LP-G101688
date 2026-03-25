import os 

os.system("cls")

# criando um vetor
vetor_notas = []
QUANTIDADE_NOTAS = 3

print("adicionando 3 notas.")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"digite {i+1}° nota: "))
    vetor_notas.append(nota)
    
print("\nexibindo notas informadas.")
# foreach.
for uma_nota in vetor_notas:
    print(f"nota: {uma_nota}")