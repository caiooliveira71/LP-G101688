import os 

os.system("cls")

codigo = [1,2,3,4,5]
prato = ["picanha","lasanha","strogonoff","bife acebolado","pão com ovo"]
valores = [25,20,18,15,5]
soma_valor = 0
pedidos = []

while True:
    print("""
    === MENU ===
    1   Picanha          R$ 25,00
    2   Lasanha          R$ 20,00
    3   Strogonoff       R$ 18,00
    4   Bife acebolado   R$ 15,00
    5   Pão com ovo      R$ 15,00
        """)
    
    opção = int(input("digite o codigo do prato desejado: "))
    codigo.append(opção)
    
    match opção:
        case 1|2|3|4|5:
            indice = opção - 1
            pedidos.append(indice)
            soma_valor += valores[indice]
            print(f"{prato[indice]} adicionado!")
        case _:
            print("prato não encontrado!")
    
    mais_pedidos = input("deseja escolher outro prato?\n Use V or N:").lower()
    
    if mais_pedidos == "n":
        break

print(f"\nPratos comprados:")
for i in pedidos:
    print(prato[i])
print(f"Valor total dos pratos é {soma_valor}")
