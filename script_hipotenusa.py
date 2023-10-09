#!/usr/bin/env python3
import sys

#verificação da utilização do programa - 2 argumentos como lados de um triangulo
if len(sys.argv) != 3:
    #resposta de erro - apenas um valor passado ou mais do que um
    print("O programa é utilizado da maneira: ./script_hipotenusa.py A B, onde A e B são lados de um triangulo retângulo")
else:
    try:
        #verificação da utilização do programa - lados devem ser números inteiros
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        #verificação da utilização do programa - lados devem ser menores do que 500
        if (a < 500) and (b < 500):
            c = a**2 + b**2
            print(f"O quadrado da hipotenusa para o triangulo retângulo com lados a = {a} e b = {b} é {c}")
        else:
            #resposta de erro - lados maiores do que 500
            print("Os lados do triangulo retângulo devem ser menores do que 500!")
    except ValueError as e:
        #resposta de erro - lados não inteiros
        print(f"Garanta que o valores dos lados sejam inteiros! Erro: {e}")


