print("menu")
print("""
      
      ========== Menu ==========
      1    picanha    R$25,00
      2    lasanha    R$20,00
      3  strogonoff   R$18,00
      4  bife acebolado R$15,00
      5  pão com ovo  R$5,00    
      
      
      """)
prato = input("digite o codigo do prato: ")

match prato:
    case "prato1":
        print("picanha/valor R$ 25,00")
    case "prato2":
        print("lasanha/valor R$20,00")
    case "prato3":
        print("strogonoff/valor R$18,00")
    case "prato4":
        print("bife acebolado/valor R$15,00")
    case "prato5":
        print("pão com ovo/valor R$5,00")
    case _:
        print("invalido")