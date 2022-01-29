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
print(len(word))
occursions = {}
for i in word:
    occursions.update({i:word.count(i)})
def FindPlace(data,frequency):
    flag = 0
    for i in range(len(data)):
        if data[i].freq.dane >= frequency:

            flag = i - 1
            return flag
        else:
            continue
    print('nie znaleziono większego')
    return len(data)-1


def CreateHuffmanTree(nodes_list):
    tmp_znak = '_'
    head = nodes_list[0]
    tail = nodes_list[-1]
    while head != tail:
        nowe_dane = head.freq.dane + head.next.freq.dane
    return nodes_list
def SimpleHuffman(slowo):
    drzewa_symboli = []
    for symbole in occursions.keys():
        tmp = Drzewo_huffmana(symbole,occursions[symbole])
        drzewa_symboli.append(tmp)

    drzewa_symboli.sort(key= lambda x: x.dane)
    zestaw_list = []
    for i in drzewa_symboli:
        tmp = HuffmanList(i)
        zestaw_list.append(tmp)
    for i in range(len(zestaw_list)):
        try:
            zestaw_list[i].next = zestaw_list[i+1]
            zestaw_list[i].previous = zestaw_list[i-1]
        except IndexError:
            if i == 0:
                zestaw_list[i].next = zestaw_list[i+1]
                zestaw_list[i].previous = None
            if i == len(zestaw_list)-1:
                zestaw_list[i].next = None
                zestaw_list[i].previous = zestaw_list[i-1]
    ostateczna = CreateHuffmanTree(zestaw_list)
    tmp_znak = ''
    #print(ostateczna)
    ostateczna.DFS(ostateczna)




SimpleHuffman(word)