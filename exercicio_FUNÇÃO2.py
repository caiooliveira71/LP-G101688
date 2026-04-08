import os 

os.system("cls")

def logo():
    os.system("cls")
    print("=====")
    print("SENAI")
    print("====")


def converção(num):
    converção = num * 100 
    return converção


print("-Solicitando Dados-")
num = float(input("digite um numero em metros: "))

centimetro = converção(num)

print(f"Converção de m para cm: {centimetro}cm")