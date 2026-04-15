import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")


def calcular_imc(p,a):
    return p / (a * 2)


def verificar_imc(imc):
    if imc < 18.5:
        resultado = "ABAIXO DO PESO"
    elif 18.5 <= imc < 25:
        resultado = "PESO NORMAL"
    elif 25 <= imc < 30:
        resultado = "SOMBREPESO"
    elif 30 <= imc < 35:
        resultado = "OBESIDADE GRAU 1"
    elif 35 <= imc < 40:
        resultado = "OBESIDADE GRAU 2"
    elif imc >= 40:
        resultado = "OBESIDADE GRAU 3"
    return resultado

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
nomes_completos = []
idades = []
alturas = []
pesos = []
imcs = []
verificação = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    sobrenome = input("Digite o sobrenome do usuario: ")
    nome_completo = f"{nome} {sobrenome}"
    
    # Verificando se o usuário quer sair
    if nome.lower() == "sair":
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    nomes_completos.append(nome_completo)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

    imc = calcular_imc(peso,altura)
    verificar = verificar_imc(imc)
    imcs.append(imc)
    verificação.append(verificar)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome Completo:",nomes_completos[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"IMC DO USUARIO:", imcs[i])
    print(f"RESULTADO DO IMC:", verificação[i])
