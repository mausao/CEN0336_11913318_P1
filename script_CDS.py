#!/usr/bin/env python3
import sys
#vrificação da utilização do programa - 7 argumentos passados
if len(sys.argv) != 8:
    print("O programa é utilizado da maneira: script_CDS.py seqDNA n1 n2 n3 n4 n5 n6 - onde n1-6 são CDS de uma sequência de DNA")
else:
    try:
        #verificação da utilização do programa - primeiro argumento [1] como string (sequência de DNA)
        seqDNA = str(sys.argv[1])
        #verificação da utilização do programa - segundo ao sétimo argumento [2-7] como inteiros que representam começo e fim de uma CDS
        n1 = int(sys.argv[2])
        n2 = int(sys.argv[3])
        n3 = int(sys.argv[4])
        n4 = int(sys.argv[5])
        n5 = int(sys.argv[6])
        n6 = int(sys.argv[7])
        cds1 = n2 - n1
        cds2 = n4 - n3
        cds3 = n6 - n5
        #resposta de erro - nenhuma CDS pode ser maior que a própria sequência de DNA
        if ((cds1 > len(seqDNA)) or (cds2 > len(seqDNA)) or (cds3 > len(seqDNA))):
            print("O tamanho de alguma CDS é maior do que a sequência de DNA cedida...")
        else:
            seqCDS1 = seqDNA[n1-1:n2]
            if seqCDS1.startswith('ATG'):
                print("A primeira CDS começa com ATG - start códon")
                seqCDS2 = seqDNA[n3-1:n4]
                seqCDS3 = seqDNA[n5-1:n6]
                if ((seqCDS3[-3:] == "TAG") or (seqCDS3[-3:] == "TAA") or (seqCDS3[-3:] == "TGA")):
                    print("A última CDS termina com TAG/TAA/TGA - possíveis stop codóns")
                    print("A sequência completa da CDS fornecida é:", seqCDS1 + seqCDS2 + seqCDS3)
                    seqCDStotal = seqCDS1 + seqCDS2 + seqCDS3
                    print(len(seqCDStotal))
                    if len(seqCDStotal) % 3 != 0:
                        #resposta de erro - caso o usuário por exemplo escolha os valores de CDS como a do exemplo de teste cedido no enunciado, ou até mesmo 20 29 32 49 51 60 a quantidade de nt não se torna multipla de 3, sendo que a sequência de aminoácidos não fará sentido
                        print("A CDS indicada não apresenta a quantidade de trincas corretas - cuidado!")
                else:
                    #resposta de erro - a última CDS deve terminar em um stop códon
                    print("A última CDS deve terminar com um stop códon! (TAG/TAA/TGA)")
            else:
                #resposta de erro - a primeira CDS deve iniciar-se com um start códon
                print("A primeira CDS deve iniciar a partir de um start códon! (ATG)")
    except ValueError as e:
        #resposta de erro - primeiro argumento [1] como string e os demais [2-7] como inteiros
        print("Digite valores válidos para a sequência de DNA (string) e para as CDS (inteiros)! Erro... {e}")

