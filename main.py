import math
import numpy as np
import sys
import time

#pasa el taulell a INT
def taulellStringToINT(taulell):
    linea = []
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

# archius en el que agafarem les dades
def seleccioTest(opcio):
    if opcio == "2":
        crossword = "crossword_A_v2.txt"
        diccionari = "diccionari_A.txt"
    else:
        crossword = "crossword_CB_v2.txt"
        diccionari = "diccionari_CB_v2.txt"

    return obtenirTaulell(crossword), diccionari

def classificarDiccionari(dicpath):
    dic = {}
    for paraula in open(dicpath):
        

if __name__ == '__main__':
    opcio = input("1.Petit\n2.Gran\nEscoje opció (qualsevol altre numero escull la petita): ")
    taulell, dicpath = seleccioTest(opcio)

    tempsTrigat = time.time()

    dic = classificarDiccionari(dicpath)
    imprimirTaulell(taulell)



