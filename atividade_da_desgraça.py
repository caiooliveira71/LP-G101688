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
    salario_final = salario_bruto - desconto
    return salario_final, desconto


def calcular_salario_com_dependentes(salario_bruto, quantidade_dependentes):
    desconto_por_dependente = 150.00
    
    desconto_total = quantidade_dependentes * desconto_por_dependente
    salario_final = salario_bruto - desconto_total
    
    return salario_final, desconto_total


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
    return imposto, aliquido


while True:
    logo()
    login()
    salario_base1 = salario_base()

    pergunta = input("Deseja receber vale transporte? \ Use S ou N: ")

    if pergunta == "N":
        print("VALE TRANSPORTE NÃO ESCOLHIDO!")
    else:
        desconto = 0.6 * salario_base1
        final = salario_base1 - desconto
    
    vale_refeição = int(input("digite o valor do vale refeição da empresa: "))
    dependentes = int(input("digite a quantidade de dependentes do funcionario: "))

    salario_final, desconto = calcular_salario_com_vale(salario_base1, vale_refeição)
    salario_final_planosaude, dependente = calcular_salario_com_dependentes(salario_base1, dependentes)
    salario_final_inss = INSS(salario_base1)
    imposto, aliquido = IRRF(salario_base1)

    salario_liquido = salario_base1 - imposto - dependente - desconto - salario_final_inss
    break

print(f"SALARIO LIQUIDO COM OS DESCONTOS: {salario_liquido}")