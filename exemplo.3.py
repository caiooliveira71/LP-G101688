import os 

os.system("cls")

# criando um vetor
vetor_notas = []
QUANTIDADE_NOTAS = 3
soma = 0

print("adicionando 3 notas.")
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"digite {i+1}° nota: "))
    soma += nota
    vetor_notas.append(nota)
# sum(notas) = soma todos os valoris dos vetores
media = sum(vetor_notas) / QUANTIDADE_NOTAS
# media = soma / QUANTIDADE_NOTAS
    
print("\nexibindo notas informadas.")
# foreach = percorre o vetor sem informar a quantidade
# enumerate = atraves da variavel i, numera a quantidade de repeticões
for i, uma_nota in enumerate(vetor_notas, start=1):
    print(f"{i}° nota: {uma_nota}")
    
print(f"media das notas: {media}")