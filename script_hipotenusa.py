#!/usr/bin/env python3
import sys
if len(sys.argv) != 3:
    print("O programa é utilizado da maneira: ./script_hipotenusa.py A B, onde A e B são lados de um triangulo retângulo")
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        if (a < 500) and (b < 500):
            c = a**2 + b**2
            print(f"O quadrado da hipotenusa para o triangulo retângulo com lados a = {a} e b = {b} é {c}")
        else:
            print("Os lados do triangulo retângulo devem ser menores do que 500!")
    except ValueError as e:
        print(f"Garanta que o valores dos lados sejam inteiros! Erro: {e}")


