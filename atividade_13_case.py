num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))
caracter = input("digite um caracter(+*/-): ")


match caracter:
    case "caracter1":
        resultado = num1 + num2
    case "caracter2":
        resultado = num1 - num2
    case "caracter3":
        resultado = num1 * num2
    case "caracter4":
        resultado = num1 / num2
    case _:
        print("invalído")
        
print(f"resultado: {resultado}")

