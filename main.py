import numpy as np
from drzewa import *
word = 'Arrived compass prepare an on as. Reasonable particular on my it in sympathize. Size now easy eat hand how. Unwilling he departure elsewhere dejection at. Heart large seems may purse means few blind. Exquisite newspaper attending on certainty oh suspicion of. He less do quit evil is. Add matter family active mutual put wishes happen.'
occursions = {}
prawdopodobienstwa = {}
for i in word:
    occursions.update({i:word.count(i)})

def TreeListSort(tree_list):
    return sorted(tree_list,key= lambda  x: x.ZwrocKorzen()[1])

def Huffman(slowo):
    drzewa_symboli = []
    for symbole in occursions.keys():
        drzewa_symboli.append(Drzewo((symbole,occursions[symbole])))
    #drzewa_symboli.sort(key = lambda x:x[1].ZwrocKorzen())
    posortowane_drzewa = TreeListSort(drzewa_symboli)

    while len(posortowane_drzewa) > 1:
        nowe_drzewo = posortowane_drzewa[0].DodawanieDrzew(posortowane_drzewa[1])
        posortowane_drzewa.pop(0)
        posortowane_drzewa.pop(0)
        posortowane_drzewa.append(nowe_drzewo)

        posortowane_drzewa = TreeListSort(posortowane_drzewa)

    #print(posortowane_drzewa[0].ZwrocDzieci(('afg',10)))
    posortowane_drzewa[0].Generator_wykresu()
Huffman(word)
