import os 


# FUNÇÃO SEM PARAMETRO E SEM RETORNO
def logo():
    os.system("cls")
    print("=====")
    print("SENAI")
    print("=====")

# FUNÇÃO COM PARAMETRO E COM RETORNO
def somar(a, b):
    return a + b 


def sub(a,b):
    return a - b


def mult(a,b):
    multiplicação = a*b
    print(f"Mutiplicação: {multiplicação}")


def divizao(a,b):
    dividir = a/b
    print(f"divizão: {dividir}")


def media(a,b):
    soma = a+b
    return soma / 2


def converção(a):
    valor = float(input("digite um valor em metros: m"))
    converção = a / 100
    return 

numero = []

print("-Solicitando Dados-")
for i in range(2):
    num = int(input("digite um numero: "))
    numero.append(num)

num1 = numero[0]
num2 = numero[1]

soma = somar(num1,num2)
subtração = sub(num1,num2)
media = media(num1,num2)

logo()
print("Exibindo dados")
print(f"Soma: {soma}")
print(f"Subtração: {subtração}")
divizao(num1,num2)
mult(num1,num2)
print(f"Media: {media}")

if media >= 7:
    print("APROVADO")
if 5 <= media < 7:
    print("RECUPERAÇÃO")
if media < 5:
    print("REPROVADO")

