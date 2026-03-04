dia = input("digite um dia: ")

match dia:
    case "segunda":
        print("segunda")
    case "terça":
        print("terça")
    case "quarta":
        print("quarta")
    case "quinta":
        print("quinta")
    case "sexta":
        print("sexta")
    case "sabado":
        print("sabado")
    case "domingo":
        print("domingo")
    case _:
        print("dia invalido")