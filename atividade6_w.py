import os 

os.system("cls")

while True:
    prato = int(input("digite o numero do seu prato"))
    match prato:
        case 1:
            prato = "picanha"
            preco = 25
        case 2:
            prato = "lasanha"
            preco = 20
        case 3:
            prato = "stogonoff"
            preco = 18
        case 4:
            prato = "bife acebolado"
            preco = 15
        case 5:
            prato = "pão com ovo"
            preco = 5
        case _:
            print("opção invalida")
            print("...tenta novamente")
            
    preco_total += preco
    pratos_solicitados += ", " + prato if  pratos_solicitados else prato

    mais_pedidos = input("deseja fazer outro pedido? \nUse S ou N: ").lower()

    if mais_pedidos == "n":
        break
    total_pagar = preco_total
    
print(f"pratos solicitados: {pratos_solicitados}")
print(f"total da compra: {preco_total}")
