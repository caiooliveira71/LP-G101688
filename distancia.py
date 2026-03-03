import os

os.system("cls")

medida = float(input("digite a distancia em metros: "))

cm = medida * 100
mm = medida * 1000

print("a medida de {}m correspondi a {}cm e {}mm".format(medida, cm, mm))
