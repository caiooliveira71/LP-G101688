import os 

os.system("cls")

matriculas = []
senhas = []
salarioarray = []


def logo():
    os.system("cls")
    print("----------------------------------")
    print(" SISTEMA DE FOLHA DE PAGAMENTO")
    print("----------------------------------")


def login():
    matricula = input("digite sua matricula: ")
    matriculas.append(matricula)
    senha = input("digite sua senha: ")
    senhas.append(senha)


def salario_base():
    salario = float(input("digite o salario base do funcionario:"))
    salarioarray.append(salario)
    return salario


def calcular_salario_com_vale(salario_bruto, valor_vale):
    desconto = valor_vale * 0.20
    return desconto


def calcular_salario_com_dependentes(salario_bruto, quantidade_dependentes):
    desconto_por_dependente = 150.00
    
    desconto_total = quantidade_dependentes * desconto_por_dependente
    
    return desconto_total


def INSS(salario):
    inss = 0.0

    if salario > 4190.83:
        base = min(salario, 8157.41) - 4190.83
        inss += base * 0.14
    if salario > 2793.88:
        base = min(salario, 4190.83) - 2793.88
        inss += base * 0.12
    if salario > 1518.00:
        base = min(salario, 2793.88) - 1518.00
        inss += base * 0.09
    if salario > 0:
        base = min(salario, 1518.00)
        inss += base * 0.075
    if inss > 951.62:
        inss = 951.62
    return inss
        

def IRRF(salario):
    if salario <= 2428:
        aliquido = 0.0
    if 2428 < salario <= 2826:
        aliquido = 0.075        
    if 2826 < salario <= 3751:
        aliquido = 0.15       
    if 3751 < salario <= 4664:
        aliquido = 0.225
    if salario > 4664:
        aliquido = 0.275
    
    imposto = salario * aliquido
    return imposto


while True:
    logo()
    login()
    salario_base1 = salario_base()

    pergunta = input("Deseja receber vale transporte? \ Use S ou N: ")

    if pergunta == "N":
        print("VALE TRANSPORTE NÃO ESCOLHIDO!")
    else:
        desconto_transporte = 0.06 * salario_base1
        
    vale_refeição = int(input("digite o valor do vale refeição da empresa: "))
    dependentes = int(input("digite a quantidade de dependentes do funcionario: "))

    salario_final_refeição = calcular_salario_com_vale(salario_base1, vale_refeição)
    salario_final_planosaude = calcular_salario_com_dependentes(salario_base1, dependentes)
    salario_final_inss = INSS(salario_base1)
    salario_final_irrf = IRRF(salario_base1)

    soma_desconto = salario_final_irrf + salario_final_planosaude + salario_final_inss + desconto_transporte + salario_final_refeição
    salario_liquido = salario_base1 - soma_desconto
    break

print("\n--- RESUMO DA FOLHA ---")
print(f"Salário Bruto: R$ {salario_base1:.2f}")
print(f"INSS: R$ {salario_final_inss:.2f}")
print(f"IRRF: R$ {salario_final_irrf:.2f}")
print(f"Vale Transporte: R$ {desconto_transporte:.2f}")
print(f"Vale Refeição (desconto): R$ {salario_final_refeição:.2f}")
print(f"Plano de Saúde: R$ {salario_final_planosaude:.2f}")
print(f"Total de Descontos: R$ {soma_desconto:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")