import copy
import math
import numpy as np
import sys
import time
# https://plugins.jetbrains.com/plugin/16536-line-profiler
from line_profiler_pycharm import profile

#pasa el taulell a INT
def taulellStringToINT(taulell):
    result = []
    for j in range(0, (len(taulell))):
        linea = taulell[j].split()

        if "#" in linea:
            for index, element in enumerate(linea):
                if element == '#':
                    linea[index] = "-1"

        linea = np.array(linea, dtype=(int))
        result.append(linea)
    return result

#pasa el taulell a String
def taulellINTtoString(taulell):
    linea = []
    result = []
    for j in range(0, (len(taulell))):
        linea = taulell[j]
        linea[linea == -1] = 35
        linea = linea.tostring().decode("ascii")
        linea = list(linea)
        result.append(linea)
    return result

# Obtenim el taulell
def obtenirTaulell(crosswordFile):
    taulell = []
    for linea in open(crosswordFile):
        taulell.append(linea)
    return taulellStringToINT(taulell)

#Impresió del taulell
def imprimirTaulell(taulell):
    for i in range(0,len(taulell)):
        for j in range(0,len(taulell[i])):
            sys.stdout.write(taulell[i][j])

# arxius dels que s'agafen les dades
def seleccioTest():

    crossword = "crossword_CB_v2.txt"
    diccionari = "diccionari_A.txt"

    return obtenirTaulell(crossword), diccionari

@profile
def classificarDiccionari(dicpath):

    dic = {}
    for linies in open(dicpath):
        paraula = linies.split('\n')[0]

        mida = len(paraula)
        byteArr = bytearray(paraula, 'ansi')
        asciiWord = []
        for letter in byteArr:
            asciiWord.append(letter)
        asciiWordNp = np.array(asciiWord, dtype=np.uint8)

        if mida in dic:
            nparr = np.append(dic[mida], asciiWordNp)
            dic[mida] = nparr
        else:
            nparr = np.array([], dtype=np.uint8)
            nparr = np.append(nparr, asciiWordNp)
            dic[mida]=nparr

    for k, v in dic.items():
        v = np.reshape(v, (-1, k))
        dic[k] = v

    return dic


if __name__ == '__main__':
    taulell, dicpath = seleccioTest()


    start = time.time()

    dic = classificarDiccionari(dicpath)


    end = time.time()
    temps = end-start
    print("temps: %d", temps)




