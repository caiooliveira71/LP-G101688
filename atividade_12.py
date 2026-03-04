sexo = input("digite seu sexo: ")
ano_de_nascimento = int(input("digite seu ano de nascimento: "))

idade = 2026 - ano_de_nascimento

if sexo == "M" and idade >= 18:
    print("serviso obrigatorio")
else:
    print("não deve se apresentar")