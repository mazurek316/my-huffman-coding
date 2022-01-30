import numpy as np

import drzewa_serie
from drzewa_serie import *
from additional_classes import *
filename = input("podaj nazwe pliku: ")
word = ''
file = open(filename,'r')
word = file.read()
file.close()

print(word)
for i in word:
    i = i.capitalize()
occursions = {}
for i in word:
    occursions.update({i:word.count(i)})

def find(list_of_vectors,vector):
    for i in list_of_vectors:
        if i.symbol == vector.symbol and i.runLen == vector.runLen:
            return list_of_vectors.index(i)
        else:
            continue
    return len(list_of_vectors) - 1

def garnerData(data):
    znak1 = ''
    znak2 = ''
    data_vector = []
    i = 1
    j = 0
    while i != len(data):
        r = DataRec()
        znak1 = data[i]
        znak2 = data[i-1]
        if znak1 == znak2:
            j = i
            r.symbol = znak2
            #print(znak1,znak2)
            while znak1 == znak1:

                r.runLen += 1
                j += 1
                try:
                    znak1 = data[j]
                except IndexError:
                    #print(j,len(data))
                    break

        else:
            r.symbol = znak1
            r.runLen = 1
            if find(data_vector, r) != len(data_vector) - 1:
                tmp = find(data_vector, r)
                data_vector[tmp].freq += 1
            else:
                r.freq += 1
                data_vector.append(r)

        i += 1


    return data_vector
Data = garnerData(word)
for i in Data:
    print(i.symbol,i.runLen,i.freq)






def CreateHuffmanTree(nodes_list):
    tmp_znak = '_'
    head = nodes_list[0]
    tail = nodes_list[-1]
    p = head
    while p.next is not None:
        tmp = p.next
        #print(p.freq.znak, 'nastepny: ', tmp.freq.znak, tmp.freq.dane)
        p = tmp
    while head != tail:
        nowe_dane = head.freq.Dodaj(head.freq.znak+head.next.freq.znak,head.next.freq)


        tmp_znak += '_'
        p = tail
        while p is not None and p.freq.dane >= nowe_dane.dane:

            tmp = p.previous
            p = tmp

        nowa_lista = HuffmanList(None, poprzedni=p,nast=p.next)

        p.next = nowa_lista
        if p == tail:
            tail = nowa_lista
        else:
            nowa_lista.next.previous = nowa_lista
        nowa_lista.freq = nowe_dane
        head = head.next.next
        #print(head.next,head.previous)
        try:
            del head.previous.previous
            del head.previous
        except AttributeError:
            if head.previous is None:
                break
        head.previous = None
    HuffmanTree = head.freq
    #print('-----------')
    #HuffmanTree.DFS(HuffmanTree)
    return HuffmanTree

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
    #ostateczna.DFS(ostateczna)




SimpleHuffman(word)