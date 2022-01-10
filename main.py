import numpy as np
from drzewa import *
word = 'aaaaacccccccccccccccccccccggggeeeeeeeeef'
occursions = {}
prawdopodobienstwa = {}
for i in word:
    occursions.update({i:word.count(i)})
    prawdopodobienstwa.update({i:occursions[i]/len(word)})

prawdopodobienstwa_do_liczenia = [*prawdopodobienstwa.values()]


def Huffman(slowo):
    occursions = {}
    prawdopodobienstwa = {}
    for i in slowo:
        occursions.update({i:slowo.count(i)})
        prawdopodobienstwa.update({i:occursions[i]/len(slowo)})
    drzewa_huffmana = {}
    tmp_drzewa = []
    for i in prawdopodobienstwa.values():
        tmp_drzewo = Drzewo(str(i))
        drzewa_huffmana.update({i:tmp_drzewo})
        tmp_drzewa.append(i)
    tmp_drzewa.sort()
    tmp_drzewa2 = []
    for i in tmp_drzewa:
        tmp_drzewa2.append(drzewa_huffmana[i])
    
    while len(tmp_drzewa2) > 1:
        #print(tmp_drzewa2[0].ZwrocKorzen(),tmp_drzewa2[1].ZwrocKorzen())
        nowe_drzewo = tmp_drzewa2[0].DodawanieDrzew(tmp_drzewa2[1])
        tmp_drzewa2.pop(0)
        tmp_drzewa2.pop(0)
        tmp_drzewa2.append(nowe_drzewo)
    tmp_drzewa2[0].Generator_wykresu()
Huffman(word)
