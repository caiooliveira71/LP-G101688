import os 
import time

os.system("cls")

num = int(input("digite um numero: "))

for i in range(num,0,-1):
    print(i)
    time.sleep(1)