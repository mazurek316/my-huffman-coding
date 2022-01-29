import numpy as np
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
    while len(drzewa_symboli) > 1:

        nowe_dane = drzewa_symboli[0].dane + drzewa_symboli[1].dane
        nowe_drzewo = Drzewo_huffmana(None,nowe_dane,drzewa_symboli[0],drzewa_symboli[1])
        drzewa_symboli.append(nowe_drzewo)
        drzewa_symboli.pop(0)
        drzewa_symboli.pop(0)
        drzewa_symboli.sort(key = lambda x: x.dane)
    koncowe = drzewa_symboli[0]
    koncowe.DFS_with_kids(koncowe.lewy)
    koncowe.Krawedzie(koncowe)
    print(koncowe.Krawedzie_test())



SimpleHuffman(word)