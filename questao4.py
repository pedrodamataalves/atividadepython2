from typing import Iterable

def soma(argumento1, argumento2, argumento3):
    return(argumento1 + argumento2 + argumento3)
umNome = input ('Qual seu nome?')
arg1 = input(f"Quantos anos tem sua mãe {umNome}? ")
arg1 = int(arg1)
arg2 = input(f"Quantos anos tem seu pai {umNome}? ")
arg2 = int(arg2)
arg3 = input(f"Quantos anos você tem {umNome}? ")    
arg3 = int(arg3)

print(f"Logo se a idade do teu pai é {arg2}, da sua mãe {arg1} e a tua {arg3} ")

print("A soma da idade dos três será: ",soma(arg1, arg2, arg3) )

