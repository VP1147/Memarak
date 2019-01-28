from random import randint
import csv
import os
import re

pattern_int = re.compile(r"(0|-?[1-9][0-9]*)")

with open('./options.csv') as data:
    readcsv = csv.reader(data, delimiter=';')
    for row in readcsv:
        vmin = row[0]
        vmax = row[1]
        vmin = int(vmin)
        vmax = int(vmax)

aritpath = './aritmodeConfig.txt'
aritOpt = open(aritpath, 'r')
aritModeVar = aritOpt.read()
aritOpt.close()
print("<Digite \'exit\' para sair>")
if aritModeVar == '1':
    while 1:
        x = randint(vmin,vmax)
        y = randint(vmin,vmax)
        r = str(x+y)
        xstr = str(x)
        ystr = str(y)
        z = str(input(xstr+" + "+ystr+" = "))
        if(z == r):
            print("Certo!")
        elif(z == 'exit'):
            exit()
        else:
            print("Errado, é ",x+y)

elif aritModeVar == '2':
    while 1:
        x = randint(vmin,vmax)
        y = randint(vmin,vmax)
        r = str(x-y)
        xstr = str(x)
        ystr = str(y)
        z = str(input(xstr+" - "+ystr+" = "))
        if(z == r):
            print("Certo!")
        elif(z == 'exit'):
            exit()
        else:
            print("Errado, é ",x-y)

elif aritModeVar == '3':
    while 1:
        x = randint(vmin,vmax)
        y = randint(vmin,vmax)
        r = str(x*y)
        xstr = str(x)
        ystr = str(y)
        z = str(input(xstr+" x "+ystr+" = "))
        if(z == r):
            print("Certo!")
        elif(z == 'exit'):
            exit()
        else:
            print("Errado, é ",x*y)

elif aritModeVar == '4':
    print("<Precisão de 2 decimais. 1 escreve-se 1.0")
    while 1:
        x = randint(vmin,vmax)
        y = randint(vmin,vmax)
        if x != 0 and y != 0:
            rct = float(("%.2f" % round((x/y),2)))
            r = str(rct)
            xstr = str(x)
            ystr = str(y)
            z = str(input(xstr+" : "+ystr+" = "))
            if(z == r):
                print("Certo!")
            elif(z == 'exit'):
                exit()
            else:
                print("Errado, é ",rct)
