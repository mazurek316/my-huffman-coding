import math
from drzewa import *
file = open('dane.txt','rt')
word = file.read()
file.close()
occursions = {}
prawdopodobienstwa = {}
for i in word:

    occursions.update({i:word.count(i)})
occursions.update({'SPACE':occursions[' ']})
occursions.pop(' ')

def TreeListSort(tree_list):
    return sorted(tree_list,key= lambda  x: x.ZwrocKorzen()[1])

def Zakodowanie_danych(dane,kody):
    zakodowane = []
    for i in dane:
        zakodowane.append(kody[i])
    #wynik = ''.join([str(i) for i in zakodowane])
    wynik = ''.join([str(i) for i in zakodowane])
    #print(len(wynik)/8)
    wynik_bytes = int(wynik,2).to_bytes(math.ceil(len(wynik)/8),'little')
    return wynik_bytes







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
    #posortowane_drzewa[0].Generator_wykresu()
    koncowe = posortowane_drzewa[0]

    #koncowe.Generator_wykresu()
    #print(koncowe.ZwrocDzieci(('wo',2)))
    koncowe.OznaczanieWezla(koncowe.ZwrocKorzen(),'')
    kody = koncowe.ZwrocKody()
    #print(kody)
    result = Zakodowanie_danych(slowo,kody)
    file = open('dane_koncowe.txt','wb')
    file.write(result)
    file.close()

    print('poczatkowe slowo w bajtach: ',len(slowo))
    print('koncowe w bajtach: ',len(result))
    return kody
slownik = Huffman(word)
def Dekodowanie_huffmana(plik,dictionary):
    file = open(plik,'rb')
    zakodowana = file.read()
    file.close()
    decoded = format(int.from_bytes(zakodowana,'little'),'023b')

    res = ""
    while decoded:
        for k in dictionary:
            if decoded.startswith(dictionary[k]):
                res += k
                decoded = decoded[len(dictionary[k]):]
    return res

zdekodowana = Dekodowanie_huffmana('dane_koncowe.txt',slownik)

dekodowany_plik = open('odkowanane.txt','wt')
dekodowany_plik.write(zdekodowana)
dekodowany_plik.close()
