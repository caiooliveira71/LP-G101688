primeira_nota = float(input("digite sua primeira nota:"))
segunda_nota = float(input("digite sua segunda nota:"))
terceira_nota = float(input("digite a terceira nota:"))

media = (primeira_nota + segunda_nota) / 2

if media <= 7:
    print(f"{media} ELE ESTA APROVADO.")
else:
    print(f"{media} ELE ESTA REPROVADO.")
    
print(f"Media: {media}")

