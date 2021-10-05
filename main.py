import copy
import math
import numpy as np
import sys
import time

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
    diccionari = "diccionari_CB_v2.txt"

    return obtenirTaulell(crossword), diccionari

def classificarDiccionari(dicpath):

    dic = {}
    for linies in open(dicpath):
        paraula = linies.split('\n')

        mida = len(paraula)

        bArr = bytearray(paraula, 'utf8')
        asciiWord = []
        for letter in bArr:
            asciiWord.append(letter)
        asciiWordNp = np.array(asciiWord, dtype=np.int8)



        if mida in dic:
            dic[mida] = np.array([], dtype=np.int8)
        else:
            dic[mida] = np.array([], dtype=np.int8)



    return dic


if __name__ == '__main__':
    taulell, dicpath = seleccioTest()


    tempsTrigat = time.time()

    dic = classificarDiccionari(dicpath)




