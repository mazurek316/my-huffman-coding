import numpy as np
import  re
import drzewa_serie
from drzewa_serie import *
from additional_classes import *
matcher = re.compile(r'(.)\1*')
import bitarray
ba = bitarray.bitarray()

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
try:
    occursions.update({'SPACE':occursions[' ']})
    occursions.pop(' ')
except KeyError:
    pass


def find(list_of_vectors,vector):
    for i in list_of_vectors:
        if i == vector:
            return list_of_vectors.index(i)

        else:
            continue
    return len(list_of_vectors) - 1

def garnerData(data):
    znak1 = data[0]
    znak2 = ''
    data_vector = []
    i = 0
    j = 0


    x = [match.group() for match in matcher.finditer(data)]
    for i in x:
        r = DataRec()
        if len(i) > 1:
            r.symbol = i[0]
        else:
            r.symbol = i
        r.runLen = len(i)
        r.freq = x.count(i)
        if find(data_vector,r) == len(data_vector) - 1:
            data_vector.append(r)
        else:
            continue

    return data_vector


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
        nowe_dane = head.freq.Dodaj(head.freq.znak + head.next.freq.znak,head.next.freq)

        tmp_znak += '_'
        p = tail
        while p is not None and p.freq.dane[0] > nowe_dane.dane[0]:

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

def encode(data,code_dict):
    x = [match.group() for match in matcher.finditer(data)]
    pack = ''
    for i in x:
        pack += str(code_dict[i])
        if len(pack) > 32:
            print('przekroczono dlugosc!')
            break
    full_pack = pack + '0'*(32-len(pack))
    print(full_pack,len(full_pack))
    splited = bytes(1024)
    print(splited)

    return 'done'


def SimpleHuffman(data):
    try:
        if occursions['SPACE'] > 1:
            tmp_r = DataRec('SPACE', 1, 15)
            index = (find(data, tmp_r))
            data.pop(index)
    except KeyError:
        pass
    drzewa_symboli = []


    for vector in data:
        tmp = Drzewo_huffmana(vector.symbol,(vector.freq,vector.runLen))
        drzewa_symboli.append(tmp)

    drzewa_symboli.sort(key= lambda x: x.dane[0])

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
    codes = {}
    #print(ostateczna)

    drzewa_serie.OznaczWezel(ostateczna,tmp_znak,codes)


    file = open('wynik.bin','wb')
    sorted_data = sorted(data,key= lambda x: x.freq)
    for i in sorted_data:
        tmp = [i.symbol,i.runLen,i.freq]
        byte_text = str(tmp) + ' '
        changed = bytes(byte_text,'ascii')
        file.write(changed)
    file.write(bytes("\n",'ascii'))

    file.close()

    encode(word, codes)

SimpleHuffman(garnerData(word))