import os 

os.system("clear")

nome = ["Hemograma Completo","Raio-X","Ultrassonografia","Eletrocardiograma","Tomografia","Ressonância Magnética","Exame de Glicose"]
valor = [30,15,12,100,180,320,600]
codigo = [1,2,3,4,5,6,7]
pedido = []
soma_valor = 0

while True:

    opçao = int(input("digite o codigo com o exame: "))

    match opçao:
        case 1|2|3|4|5|6|7:
            indice = opçao - 1
            pedido.append(indice)
            soma_valor += valor[indice] 
            print(f"{nome[indice]} exame adicionado!")
        case _:
            print("exame não encontrado!")

    mais = int(input("deseja adicionar outro exame?\n Use (1 para adicionar outro exame) ou (0 para encerrar programa): "))

    if mais == 0:
        break

pagamento = int(input("digite o codigo da forma de pagamento: "))

if pagamento == 1:
    desconto = soma_valor * 0.15
    final = soma_valor - desconto
if pagamento == 2:
    desconto = 0
    final = soma_valor - desconto
if pagamento == 3:
    desconto = soma_valor * 0.8
    final = soma_valor - desconto

print("\n----RESUTADO----")

for i in pedido:
    print("exame escolhido: "{nome[indice]})

for i in pedido:
    print("codigo escolhido: "{codigo[indice]})

print("Valor total sem desconto: "{soma_valor})
print("For de pagamento escolhida: "{pagamento})
print("Valor do desconto ou acrescimo: "{desconto})
print("Valor final: "{final})