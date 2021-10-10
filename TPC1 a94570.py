# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 22:08:57 2021

@author: a94570
"""
import random
def jogo():
    print("Bem vindo ao jogo 21 fósforos! Você irá jogar contra o computador(c)! ")
    n=21
    ordem=input("Quer jogar primeiro? Sim(s) ou Não(n)?")
    if ordem=="s" or ordem=="Sim":
        while n >1: 
            jogada=int(input("Quantos fósforos quer tirar, 1, 2, 3 ou 4?"))
            if jogada>=1 and jogada<=4:
                n=n-jogada
                print ("Restam", n, "fósforos! ")
                if jogada==1:
                    n=n-4
                    print("O computador retira 4 fósforos! ")
                    print("Restam", n, "fósforos!")
                if jogada==2:
                    n=n-3
                    print("O computador retira 3 fósforos!")
                    print("Restam", n, " fósforos! ")
                if jogada==3:
                    n=n-2
                    print("O computador retira 2 fósforos! ")
                    print("Restam", n, "fósoforos!")
                if jogada==4:
                    n=n-1
                    print ("O computador retira 1 fósforo! ")
                    print("Restam", n, "fósforos!")
            if jogada<1 and jogada>4: 
                print("Erro!")
        print("End of the game! You lost!") 
    if ordem=="n" or ordem=="Não":
        jogada_pc=random.randint(1,4)
        n=n-jogada_pc
        print("o computador retira", jogada_pc, "fósforos!")
        print("Restam", n, "fósforos!") 
        while n>1:
            jogada=int(input("Quantos fósforos quer tirar 1, 2, 3 ou 4?"))
            if jogada>=1 and jogada<=4:    
                n=n-jogada
                print("Restam", n, "fósforos!")   
                if n==1:
                    print("The player win! Congratulations!")
                if n==2:
                    jogada_pc=1
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                    print("The player lost!")
                if n==3:
                    jogada_pc=2
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                    print("The player lost!")
                if n==4:
                    jogada_pc=3
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                    print("O Jogador perdeu!")
                if n==5:
                    jogada_pc=4
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                    print("O Jogador perdeu!")
                if n==6:
                    jogada_pc=random.randint(1,4)
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==7:
                    jogada_pc=1
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==8:
                    jogada_pc=2
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==9:
                    jogada_pc=3
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==10:
                    jogada_pc=4
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==11:
                    jogada_pc=random.randint(1,4)
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==12:
                    jogada_pc=1
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==13:
                    jogada_pc=2
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==14:
                    jogada_pc=3
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==15:
                    jogada_pc=4
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==16:
                    jogada_pc=random.randint(1,4)
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==17:
                    jogada_pc=1
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==18:
                    jogada_pc=2
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==19:
                    jogada_pc=3
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
                if n==20:
                    jogada_pc=4
                    n=n-jogada_pc
                    print("A jogada do computador é retirar", jogada_pc, "fósforos.")
                    print("Restam", n, "fósforos!")
            if jogada<1 or jogada>4:
                print("Erro!") 
jogo()
