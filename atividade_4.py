primeiro_numero = float(input("digite o primeiro numero:"))
segundo_numero = float(input("digite o segundo numero:"))

soma = (primeiro_numero + segundo_numero)

produto = (primeiro_numero * segundo_numero)

media = (primeiro_numero + segundo_numero) / 2

# if primeiro_numero < segundo_numero:
#     print("primeiro é menor")
#     print("segundo é maior")
# if primeiro_numero > segundo_numero:
#     print("primeiro é maior")
#     print("segundo é menor")

menor = min(primeiro_numero, segundo_numero)
maior = max(primeiro_numero, segundo_numero)

print(f"soma: {soma}")
print(f"produto: {produto}")
print(f"media: {media}")
 
    
