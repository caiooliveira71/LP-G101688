import os 

os.system("cls")

soma = 0
habitantes = 0
mulheres_5000 = 0
maior_idade = 0
menor_idade = 0

while True:
    print("""CODIGO| DESCRIÇÃO
            1  | ADICIONAR PESSOA
            2  | EXIBIR RESULTADO
            3  | SAIR
      """)

    codigo = int(input("digite o codigo do menu: "))
    
    if codigo == 1:
        idade = int(input("digite sua idade: "))
        sexo = input("digite seu sexo(F/M): ")
        salario = int(input("digite seu salario: "))
    
        soma += salario
        habitantes += 1
        media = soma / habitantes
    
        if habitantes == 1:
            maior_idade = idade
            menor_idade = idade
        else:
            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade
                
        if sexo == "f" and salario >= 5000:
            mulheres_5000 += 1
        
        print("pessoa cadastrada com sucesso!")
    
    if codigo == 2:
        if habitantes == 0:
            print("pessoa não cadastrada!")
        else:   
            media = soma / habitantes
            
            print("---RESUTADO---")
            print(f"media salrial do grupo: {media}")
            print(f"maior idade do grupo: {maior_idade}")
            print(f"menor idade do grupo: {menor_idade}")
            print(f"mulheres com salario maior que 5000: {mulheres_5000}")
            
    if codigo == 3:
        print("programa encerrado!")
        break
            
        
        
        
        