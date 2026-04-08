import os 

os.system("cls")

def idade(a):
    idade = 2026 - a
    return idade


ano_nascimento = int(input("digite seu ano de nascimento: "))

idade = idade(ano_nascimento)

print(f"Idade do usuario: {idade}")