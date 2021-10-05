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
def classificarDiccionari(dictPath):

    # Dictionary with all the words.
    # Each key is the size of the word.
    # Each value is a 2D numpy array. The first dimension is the word,
    # the second dimension contains the letter from each word.

    dict = {}

    for line in open(dictPath):
        word = line[:-1]
        size = len(word)
        byteArr = bytearray(word, 'ansi')
        asciiWord = list(byteArr)

        if size in dict:
            dict[size].append(asciiWord)
        else:
            dict[size] = [asciiWord]

    # Transforming list into numpy array
    for k, v in dict.items():
        numpyArr = np.array(v, dtype=np.uint8)
        dict[k] = numpyArr

    return dict


if __name__ == '__main__':
    taulell, dicpath = seleccioTest()


    start = time.time()

    dic = classificarDiccionari(dicpath)


    end = time.time()
    temps = end-start
    print("temps: %d", temps)




