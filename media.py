import os


os.system("cls")

print("-solicitando dados-")

nome = input("digite seu nome:")


primeira_nota = float(input("digite a primeira nota:"))
segunda_nota = float(input("digite a segunda nota:"))
terceira_nota = float(input("digite a terceira nota:"))



media  = (primeira_nota + segunda_nota) / 2


print("\n-Exibindo dados-")
print("nome:",nome)
print(f"Media: {media} do aluno.")