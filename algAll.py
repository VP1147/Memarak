from random import randint
import csv
import os
import re

with open('./options.csv') as data:
    readcsv = csv.reader(data, delimiter=';')
    for row in readcsv:
        vmin = row[0]
        vmax = row[1]
        vmin = int(vmin)
        vmax = int(vmax)

algpath = './algmodeConfig.txt'
algOpt = open(algpath, 'r')
algmodeVar = algOpt.read()
algOpt.close()
print("<Digite \'exit\' para sair>")
if algmodeVar == '1': #caso equação
    while 1:
        x = randint(vmin,vmax)
        y = randint(vmin,vmax)
        xstr = str(x)
        ystr = str(y)
        rformat = randint(0,2)
        if rformat == 0:
            r = str(y-x)
            z = str(input("x + "+xstr+" = "+ystr+"\nx = "))
            if z == r:
                print("Certo!")
            elif z == 'exit':
                exit()
            else:
                print("Errado, é "+r)
        elif rformat == 1:
            r = str(y-x)
            z = str(input(xstr+" + x = "+ystr+"\nx = "))
            if z == r:
                print("Certo!")
            elif z == 'exit':
                exit()
            else:
                print("Errado, é "+r)
        elif rformat == 2:
            r = str(x-y)
            z = str(input(xstr+" = x + "+ystr+"\nx = "))
            if z == r:
                print("Certo!")
            elif z == 'exit':
                exit()
            else:
                print("Errado, é "+r)
