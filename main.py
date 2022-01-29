import numpy as np

import drzewa_serie
from drzewa_serie import *
from two_side_list import *
filename = input("podaj nazwe pliku: ")
word = ''
file = open(filename,'r')
word = file.read()
file.close()

print(word)

occursions = {}
for i in word:
    occursions.update({i:word.count(i)})

def SimpleHuffman(slowo):
    drzewa_symboli = []
    for symbole in occursions.keys():
        tmp = Drzewo_huffmana(symbole,occursions[symbole])
        drzewa_symboli.append(tmp)

    drzewa_symboli.sort(key= lambda x: x.dane)
    for i in drzewa_symboli: i.DFS(i)
    tmp_znak = ''
    while len(drzewa_symboli) > 1:

        if drzewa_symboli[0].dane == drzewa_symboli[1].dane:
            #print(drzewa_symboli[0].znak,drzewa_symboli[1].znak+str(drzewa_symboli[1].dane))
            drzewa_symboli[0],drzewa_symboli[1] = drzewa_symboli[1],drzewa_symboli[0]
            nowe_dane = drzewa_symboli[0].dane + drzewa_symboli[1].dane
            nowe_drzewo = Drzewo_huffmana(tmp_znak, nowe_dane, drzewa_symboli[0], drzewa_symboli[1])
            drzewa_symboli.append(nowe_drzewo)
            drzewa_symboli.pop(0)
            drzewa_symboli.pop(0)

            drzewa_symboli.sort(key=lambda x: x.dane)
            tmp_znak += ' '
        else:
            nowe_dane = drzewa_symboli[0].dane + drzewa_symboli[1].dane
            nowe_drzewo = Drzewo_huffmana(tmp_znak, nowe_dane, drzewa_symboli[0], drzewa_symboli[1])
            drzewa_symboli.append(nowe_drzewo)
            drzewa_symboli.pop(0)
            drzewa_symboli.pop(0)
            drzewa_symboli.sort(key=lambda x: x.dane)
            tmp_znak += ' '
    koncowe = drzewa_symboli[0]
    #koncowe.DFS_with_kids(koncowe)
    #koncowe.Krawedzie(koncowe)
    #print(koncowe.Krawedzie_test())
    first_code = ''
    kody = {}
    kody = drzewa_serie.OznaczWezel(koncowe,first_code,kody)
    drzewa_serie.DFS_all(koncowe,kody)

SimpleHuffman(word)