import csv
import os
import time
class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

getch = _GetchUnix()
def clearScreen():#define funcão clearScreen
    os.system('cls' if os.name == 'nt' else 'clear')

def logoType():#define função logoType
    clearScreen()
    print("███╗   ███╗███████╗███╗   ███╗ █████╗ ██████╗  █████╗ ██╗  ██╗    ██████╗ ██╗   ██╗")
    print("████╗ ████║██╔════╝████╗ ████║██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██╔══██╗╚██╗ ██╔╝")
    print("██╔████╔██║█████╗  ██╔████╔██║███████║██████╔╝███████║█████╔╝     ██████╔╝ ╚████╔╝ ")
    print("██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██╔══██║██╔══██╗██╔══██║██╔═██╗     ██╔═══╝   ╚██╔╝  ")
    print("██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██║██║  ██╗    ██║        ██║   ")
    print("╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝        ╚═╝   ")

def mainconfigOpt():#define função mainconfigOpt
    logoType()
    print("Menu -> config")
    print("1-Definir max e min\nx-Voltar")
    configOpt = getch()
    if configOpt == '1':
        logoType()
        path = './options.csv'
        options = open(path, 'w')
        options.write("0;0")
        intmin = int(input("Definir tamanho mínimo: "))
        intmax = int(input("Definir tamanho máximo: "))
        if intmin > intmax:
            print("Valores inválidos")
            time.sleep(1)
            return
        vmin = str(intmin)
        vmax = str(intmax)
        vwrite = vmin+";"+vmax
        options = open(path, 'w')
        options.write(vwrite)
    elif configOpt == 'x':
        return
    
def aritFc():
    logoType()
    print("Menu -> Jogar -> Aritmética")
    print("1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\np-Modo anterior\nx-Voltar")
    aritOpt = getch()
    if aritOpt == 'x':
        return
    elif aritOpt == 'p':
        clearScreen()
        os.system("python3 aritAll.py")
    aritpath = './aritmodeConfig.txt'
    aritOptTxt = open(aritpath, 'w')
    aritOptTxt.write(aritOpt)
    aritOptTxt.close()
    clearScreen()
    os.system("python3 aritAll.py")

def algFc():
    logoType()
    print("Menu -> Jogar -> Álgebra")
    print("1-Equação\nx-Voltar")
    algOpt = getch()
    if algOpt == 'x':
        return
    algpath = './algmodeConfig.txt'
    algOptTxt = open(algpath, 'w')
    algOptTxt.write(algOpt)
    algOptTxt.close()
    clearScreen()
    os.system("python3 algAll.py")

def mainPlayOpt():#define função mainPlayOpt
    while 1:
        logoType()
        print("Menu -> Jogar")
        print("1-Aritmética\n2-Álgebra\nx-Voltar")
        playOpt = getch()
        if playOpt == '1':
            aritFc()
        elif playOpt == '2':
            algFc()
        elif playOpt == 'x':
            return

def infoMenuOpt():
    logoType()
    print("A fazer...")
    print("x - sair")
    infoOpt = getch()
    if infoOpt == 'x':
        return
while 1:
    logoType()
    print("Menu")
    print("1-Jogar\n2-Config\n3-Sobre\nx-Sair")
    mainOpt = getch()
    if mainOpt == '1':
        mainPlayOpt()
    elif mainOpt == '2':
        mainconfigOpt()
    elif mainOpt == '3':
        infoMenuOpt()
    elif mainOpt == 'x':
        clearScreen()
        exit()
