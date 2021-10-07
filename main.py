import copy
import math
import numpy as np
import sys
import time
# https://plugins.jetbrains.com/plugin/16536-line-profiler
from line_profiler_pycharm import profile

class Word:
    def __init__(self, pos, horizontal, length):
        self.pos = pos
        self.horizontal = horizontal
        self.length = length
        #self.intersections = intersections



def read_crossword(crossword):

    table = []
    for line in open(crossword):
        noTabs = list(line.split())
        for i, v in enumerate(noTabs):
            if v == "#":
                noTabs[i] = "1"
        table.append(noTabs)
    npTable = np.array(table, dtype=np.uint8)
    return npTable

def lookupHorizontalVariables(npTable):
    foundWords = []
    for x in range(0, npTable.shape[0]):
        len = 0
        for y in range(1, npTable.shape[1]):
            if len == 0:
                if npTable[x][y-1] != 1 and npTable[x][y] != 1:
                    len = 2
                    continue
            if len > 1:
                if npTable[x][y] != 1:
                    len += 1
                    continue
                else:
                    pos = (x, y-len)
                    foundWords.append(Word(pos, 1, len))
                    len = 0

        if len > 1:
            pos = (x,npTable.shape[1]-len)
            word = Word(pos, 1, len)
            foundWords.append(word)
    return foundWords

# arxius dels que s'agafen les dades
def seleccioTest():

    crossword = "crossword_CB_v2.txt"
    diccionari = "diccionari_CB_v2.txt"

    return crossword, diccionari

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
    crosswordPath, dicPath = seleccioTest()


    start = time.time()

    crossword = read_crossword(crosswordPath)
    words = lookupHorizontalVariables(crossword)


    dic = classificarDiccionari(dicPath)


    end = time.time()
    temps = end-start
    print("temps: %d", temps)




