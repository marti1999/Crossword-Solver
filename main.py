import copy
import math
import numpy as np
import sys
import random
import time
# https://plugins.jetbrains.com/plugin/16536-line-profiler
from line_profiler_pycharm import profile

class Intersection:
    def __init__(self, coord, index, intersectedID):
        self.coord = coord
        self.index = index
        self.intersectedID = intersectedID

class Word:
    def __init__(self, pos, horizontal, length, remainingValues, idN):
        self.pos = pos
        self.horizontal = horizontal
        self.length = length
        self.remainingValues = remainingValues
        self.letters = [0] * length
        self.id = idN
        self.intersections = []
        self.intersectionsNumber = 0

# function to get the ID of a vertical word from given coordinates
# returns -1 if the word is not found
def getVerticalIdByCoordinate(coord, verticalWords):
    for w in verticalWords:
        if w.pos[1] == coord[1]:
            if w.pos[0] <= coord[0] <= w.pos[0]+w.length:
                return w.id
    return -1

# function to get the ID of a horizontal word from given coordinates
# returns -1 if the word is not found
def getHorizontalIdByCoordinate(coord, horizontalWords):
    for w in horizontalWords:
        if w.pos[0] == coord[0]:
            if w.pos[1] <= coord[1] <= w.pos[1]+w.length:
                return w.id
    return -1


def lookupIntersections(words, horizontalWords, verticalWords, crossword):
    for w in words:
        if w.horizontal == 1:
            yStart = w.pos[1]
            yEnd = yStart + w.length -1
            for y in range(yStart, yEnd+1):
                if w.pos[0] > 0:
                    if crossword[w.pos[0]-1][y] == 0:
                        index = y - w.pos[1]
                        intersectedId = getVerticalIdByCoordinate((w.pos[0], y), verticalWords)
                        w.intersections.append(Intersection((w.pos[0], y), index, intersectedId))
                        continue
                if w.pos[0] < crossword.shape[0]-1:
                    if crossword[w.pos[0]+1][y] == 0:
                        index = y - w.pos[1]
                        intersectedId = getVerticalIdByCoordinate((w.pos[0], y), verticalWords)
                        w.intersections.append(Intersection((w.pos[0], y), index, intersectedId))
        else:
            xStart = w.pos[0]
            xEnd = xStart + w.length -1
            for x in range(xStart, xEnd+1):
                if w.pos[1] > 0:
                    if crossword[x][w.pos[1]-1] == 0:
                        index = x - w.pos[0]
                        intersectedId = getHorizontalIdByCoordinate((x, w.pos[1]), horizontalWords)
                        w.intersections.append(Intersection((x, w.pos[1]), index, intersectedId))
                        continue
                if w.pos[1] < crossword.shape[1]-1:
                    if crossword[x][w.pos[1]+1] == 0:
                        index =  x - w.pos[0]
                        intersectedId = getHorizontalIdByCoordinate((x, w.pos[1]), horizontalWords)
                        w.intersections.append(Intersection((x, w.pos[1]), index, intersectedId))
        w.intersectionsNumber = len(w.intersections)

    return words


def read_crossword(crossword):
    table = []
    for line in open(crossword):
        noTabs = list(line.split())
        for i, v in enumerate(noTabs):
            if v == "#":
                noTabs[i] = "35"
        table.append(noTabs)
    npTable = np.array(table, dtype=np.uint8)
    return npTable


def storeLvaToCrossword(lva, crossword):
    for word in lva.values():
        index = 0
        if word.horizontal == 1:
            x = word.pos[0]
            for y in range(word.pos[1], word.pos[1] + word.length):
                crossword[x][y] = word.letters[index]
                index += 1
        else:
            y = word.pos[1]
            for x in range(word.pos[0], word.pos[0] + word.length):
                crossword[x][y] = word.letters[index]
                index += 1
    return crossword


def printCrossword(crossword):

    print('\n'.join([''.join(['{:4}'.format(chr(item))
                              for item in row]) for row in crossword]))
    print("\n\n")


def lookupHorizontalVariables(npTable, idN):
    foundWords = []

    for x in range(0, npTable.shape[0]):
        len = 0
        for y in range(1, npTable.shape[1]):
            if len == 0:
                if npTable[x][y - 1] != 35 and npTable[x][y] != 35:
                    len = 2
                    continue
            if len > 1:
                if npTable[x][y] != 35:
                    len += 1
                    continue
                else:
                    pos = (x, y - len)
                    foundWords.append(Word(pos, 1, len, len, idN))
                    idN += 1
                    len = 0

        if len > 1:
            pos = (x, npTable.shape[1] - len)
            word = Word(pos, 1, len, len, idN)
            idN += 1
            foundWords.append(word)
    return foundWords


def lookupVerticalVariables(npTable, idN):
    foundWords = []
    for y in range(0, npTable.shape[1]):
        len = 0
        for x in range(1, npTable.shape[0]):
            if len == 0:
                if npTable[x - 1][y] != 35 and npTable[x][y] != 35:
                    len = 2
                    continue

            if len > 1:
                if npTable[x][y] != 35:
                    len += 1
                    continue
                else:
                    pos = (x - len, y)
                    foundWords.append(Word(pos, 0, len, len, idN))
                    idN += 1
                    len = 0
        if len > 1:
            pos = (npTable.shape[0] - len, y)
            word = Word(pos, 0, len, len, idN)
            idN += 1
            foundWords.append(word)
    return foundWords


def seleccioTest():
    crossword = "crossword_CB_v2.txt"
    diccionari = "diccionari_CB_v2.txt"

    return crossword, diccionari


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

def domain(var, d):
    return d[var.length]

def restrictionsOK(var, cWord, lva, r):

    intersections = var.intersections

    for i in intersections:
        if i.intersectedID not in lva:
            continue

        intersectedWord = lva[i.intersectedID]
        candidateValue = cWord[i.index]

        if intersectedWord.horizontal == 1:
            intersectionIndex = i.coord[1] - intersectedWord.pos[1]
            intersectedValue = intersectedWord.letters[intersectionIndex]
        else:
            intersectionIndex = i.coord[0] - intersectedWord.pos[0]
            intersectedValue = intersectedWord.letters[intersectionIndex]

        if intersectedValue != candidateValue:
            return False

    return True

def insertLva(lva, var, cWord):
    var.letters = cWord.tolist()
    lva[var.id] = var
    return lva

#-----------------
# Backtraking
#------------------
def backtracking(lva, lvna, d, r):

    if not lvna:
        return lva, 1

    var = lvna[0]

    domainValues = domain(var, d)
    for cWord in domainValues:

        if restrictionsOK(var, cWord, lva, 0):
            lva = insertLva(lva, var, cWord)
            lva, r = backtracking(lva, lvna[1:], d, r)
            if r == 1:
                return lva, r

    # deleting the found value for current var if
    # it was  a dead-end on deeper calls of the function
    if r == 0 and var.id in lva:
        lva.pop(var.id)

    return lva, 0

#-----------------
# Backtraking + ForwardChecking
#------------------

def domainUpdate(var, cWord, d):

    for intersection in var.intersections:
        if cWord in d[var.length]:
            if cWord[intersection.index] == var.letters[intersection.index] or var.letters[intersection.index] == 0:
                for key in d:
                    for number,words in enumerate(d[key]):
                        if words[intersection.index] != var.letters[intersection.index]:
                            return d, True
                        d.pop(var.length, words)
                if d[key].any():
                    return d, False



def backtrackingForwardChecking(lva, lvna, d, r):

    if not lvna:
        return lva, 1

    var = lvna[0]

    domainValues = domain(var, d)
    for cWord in domainValues:

        if restrictionsOK(var, cWord, lva, 0) :
            d, modify = domainUpdate(var, cWord, d)
            if modify == True:
                lva = insertLva(lva, var, cWord)
                lva, r = backtracking(lva, lvna[1:], d, r)
                if r == 1:
                    return lva, r

    # deleting the found value for current var if
    # it was  a dead-end on deeper calls of the function
    if r == 0 and var.id in lva:
        lva.pop(var.id)

    return lva, 0

def main():
    crosswordPath, dicPath = seleccioTest()

    crossword = read_crossword(crosswordPath)

    start = time.time()
    horizontalWords = lookupHorizontalVariables(crossword, 0)
    verticalWords = lookupVerticalVariables(crossword, len(horizontalWords))

    words = horizontalWords + verticalWords
    #TODO aquesta ordenació s'ha de fer per cada nova crida del backtracking
    words.sort(key=lambda x: x.intersectionsNumber)
    #words.sort(key=lambda x: x.length)
    #random.shuffle(words)

    words = lookupIntersections(words, horizontalWords, verticalWords, crossword)

    dict = classificarDiccionari(dicPath)

    lva, r = backtrackingForwardChecking({}, words, dict, 0)

    crossword = storeLvaToCrossword(lva, crossword)
    printCrossword(crossword)

    end = time.time()
    temps = end - start
    print("temps: %d", temps)


if __name__ == '__main__':
    main()