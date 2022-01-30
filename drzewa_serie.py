from collections import defaultdict
class Drzewo_huffmana:
    def __init__(self,znak,data,lewy = None,prawy = None,ojciec = None):
        self.dane = data
        self.znak = znak
        self.lewy = lewy
        self.prawy = prawy
        self.ojciec = ojciec
    def Dodaj(self,znak, other):
        new_tree = Drzewo_huffmana(znak,self.dane+other.dane,self,other)
        return new_tree
    def DFS(self,wezel):
        if wezel:
            print(wezel.dane)
            self.DFS(wezel.lewy)
            self.DFS(wezel.prawy)
    def DFS_with_kids(self,wezel):
        if wezel:
            print(wezel.dane,'symbol: ',wezel.znak,wezel.lewy.dane,wezel.prawy.dane)
            self.DFS(wezel.lewy)
            self.DFS(wezel.prawy)

    krawedzie_lista = defaultdict(list)

    def Krawedzie(self,wezel):
        if wezel:
            #print(wezel.dane,self.lewy.dane)
            if self.lewy is not None:
                #print(wezel.lewy.dane)
                self.krawedzie_lista[wezel].append(wezel.lewy)
                self.Krawedzie(wezel.lewy)
            if self.prawy is not None:
                self.krawedzie_lista[wezel].append(wezel.prawy)
                self.Krawedzie(wezel.prawy)

    def Krawedzie_test(self):
        return self.krawedzie_lista


    def Wykres(self):
        X_wierzcholki = {}
        Y_wierzcholki = []
        X_krawedzie = []
        Y_krawedzie = []


def OznaczWezel(wezel,oznaczenie,codes):
    #print(wezel.znak,oznaczenie)
    if wezel is not None:
        codes.update({wezel.znak:oznaczenie})
        if wezel.lewy is not None:
            OznaczWezel(wezel.lewy, oznaczenie + '0',codes)
        if wezel.prawy is not None:
            OznaczWezel(wezel.prawy, oznaczenie + '1',codes)

    return codes
def DFS_all(wezel,oznaczenia):
    if wezel is not None:
        print(wezel.dane,wezel.znak,oznaczenia[wezel.znak])

        DFS_all(wezel.lewy,oznaczenia)
        DFS_all(wezel.prawy,oznaczenia)



