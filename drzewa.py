from collections import defaultdict
import collections
from typing import DefaultDict
import plotly.graph_objects as go
import numpy as np
import random


def text_wierzcholkow(tabela):
    ostateczna_tabela = []
    for i in tabela:
        if len(i[0]) > 1:
            if i[0] == 'SPACE':
                ostateczna_tabela.append(i)
            else:
                ostateczna_tabela.append(i[1])
        else:
            ostateczna_tabela.append(i)

    return ostateczna_tabela

class Drzewo:
    def __init__(self,dane):
        self.drzewo = defaultdict(list)
        self.drzewo[dane]
        self.drzewo[dane].append(None) #adres ojca
        self.drzewo[dane].append(None) #adres lewego syna
        self.drzewo[dane].append(None) # adres prawego syna
    iterator = 0
    def DodawanieDrzew(self,drugie_drzewo):


        dane1 = [*self.drzewo][0]
        dane2 = [*drugie_drzewo.drzewo][0]

        nowe_dane = dane1[1] + dane2[1]
        nowe_drzewo = Drzewo((dane1[0]+dane2[0],nowe_dane))
        if dane1[1] >= dane2[1]:
            nowe_drzewo.DodajDrzewozPrawej(self)
            nowe_drzewo.DodajDrzewozLewej(drugie_drzewo)
            return nowe_drzewo
        else:
            #print(isinstance(drugie_drzewo,Drzewo))
            nowe_drzewo.DodajDrzewozLewej(self)
            nowe_drzewo.DodajDrzewozPrawej(drugie_drzewo)
            return nowe_drzewo

    def DodajDrzewozLewej(self,drzewo_z_lewej):
        #print(dict(drzewo_z_lewej.drzewo))
        for i in drzewo_z_lewej.drzewo.keys():
            if drzewo_z_lewej.drzewo[i][0] is None:
                self.drzewo[self.ZwrocKorzen()][1] = i
                self.drzewo[i].append(self.ZwrocKorzen())
                self.drzewo[i].append(None)
                self.drzewo[i].append(None)
            else:
                tmp_ojciec = drzewo_z_lewej.drzewo[i][0]
                if i in [*self.drzewo]:
                    #print(i,tmp_ojciec,"dodaj z lewej")
                    tmp_i = (i[0],i[1]+0.1)
                    if drzewo_z_lewej.drzewo[tmp_ojciec][1] == i:
                        self.drzewo[tmp_ojciec][1] = tmp_i
                        self.drzewo[tmp_i].append(tmp_ojciec)
                        self.drzewo[tmp_i].append(None)
                        self.drzewo[tmp_i].append(None)
                    if drzewo_z_lewej.drzewo[tmp_ojciec][2] == i:
                        self.drzewo[tmp_ojciec][2] = tmp_i
                        self.drzewo[tmp_i].append(tmp_ojciec)
                        self.drzewo[tmp_i].append(None)
                        self.drzewo[tmp_i].append(None)
                else:
                    if drzewo_z_lewej.drzewo[tmp_ojciec][1] == i:
                        self.drzewo[tmp_ojciec][1] = i
                        self.drzewo[i].append(tmp_ojciec)
                        self.drzewo[i].append(None)
                        self.drzewo[i].append(None)
                    if drzewo_z_lewej.drzewo[tmp_ojciec][2] == i:
                        #print(i,self.drzewo[tmp_ojciec])
                        self.drzewo[tmp_ojciec][2] = i
                        self.drzewo[i].append(tmp_ojciec)
                        self.drzewo[i].append(None)
                        self.drzewo[i].append(None)
                
    def DodajDrzewozPrawej(self,drzewo_z_prawej):
        #print(dict(drzewo_z_prawej.drzewo))
        #print(drzewo_z_prawej.drzewo.keys())
        for i in drzewo_z_prawej.drzewo.keys():

            if drzewo_z_prawej.drzewo[i][0] is None:
                self.drzewo[self.ZwrocKorzen()][2] = i
                self.drzewo[i].append(self.ZwrocKorzen())
                self.drzewo[i].append(None)
                self.drzewo[i].append(None)
            else:
                tmp_ojciec = drzewo_z_prawej.drzewo[i][0]
                if i in [*self.drzewo]:
                    #print(i,tmp_ojciec,'z prawej')
                    tmp_i = (i[0],i[1]+0.1)
                   # print(drzewo_z_prawej.ZwrocDzieci(tmp_ojciec))
                    if drzewo_z_prawej.drzewo[tmp_ojciec][1] == i:
                       # print('lewy syn prawego')
                        self.drzewo[tmp_ojciec][1] = tmp_i
                        self.drzewo[tmp_i].append(tmp_ojciec)
                        self.drzewo[tmp_i].append(None)
                        self.drzewo[tmp_i].append(None)
                    if drzewo_z_prawej.drzewo[tmp_ojciec][2] == i:
                        #print('prawy syn prawego')
                        self.drzewo[tmp_ojciec][2] = tmp_i
                        self.drzewo[tmp_i].append(tmp_ojciec)
                        self.drzewo[tmp_i].append(None)
                        self.drzewo[tmp_i].append(None)
                else:
                    if drzewo_z_prawej.drzewo[tmp_ojciec][1] == i:
                        self.drzewo[tmp_ojciec][1] = i
                        self.drzewo[i].append(tmp_ojciec)
                        self.drzewo[i].append(None)
                        self.drzewo[i].append(None)
                    if drzewo_z_prawej.drzewo[tmp_ojciec][2] == i:
                        self.drzewo[tmp_ojciec][2] = i
                        self.drzewo[i].append(tmp_ojciec)
                        self.drzewo[i].append(None)
                        self.drzewo[i].append(None)
                

    def DodajzLewej(self,ojciec,dane):
        
        self.drzewo[dane]
        self.drzewo[dane].append(ojciec)
        self.drzewo[dane].append(None)
        self.drzewo[dane].append(None)
        self.drzewo[ojciec][1] = dane
    def DodajzPrawej(self,ojciec,dane):
        
        self.drzewo[dane]
        self.drzewo[dane].append(ojciec)
        self.drzewo[dane].append(None)
        self.drzewo[dane].append(None)
        self.drzewo[ojciec][2] = dane

    def DodajKolejny(self,dane):
        if dane in [*self.drzewo]:
            print("Błąd! istnieje już taki węzeł!")
        else:
            self.Wszystkie_Glebokosci(0)
            for i in range(max(self.glebokosci.values()) + 1):
                for k in [*self.glebokosci]:
                    if self.glebokosci[k] == i:
                    
                        if self.drzewo[k][1] is None:
                            self.drzewo[k][1] = dane
                            self.drzewo[dane].append(k)
                            self.drzewo[dane].append(None)
                            self.drzewo[dane].append(None)
                            return "done"

                        elif self.drzewo[k][2] is None:
                            self.drzewo[k][2] = dane
                            self.drzewo[dane].append(k)
                            self.drzewo[dane].append(None)
                            self.drzewo[dane].append(None)

                            return "done"
                    else:
                        continue
            


    def Generator_wykresu(self):
        węzły  = [*self.drzewo]
        
         #współrzędne x kulek
        Y_wierzcholki = [] #współrzędne y kulek
        X_krawedzie = [] #współrzędne x linii
        Y_krawedzie = [] #współrzędne y linii 
        self.Wszystkie_Glebokosci(węzły[0])
        wysokosc = (max(self.glebokosci.values())) + 2
        szerokosc = wysokosc + 10
        X_wierzcholki = {}
        
        def wspolrzedne_x(wezel,X_w):



                    ojciec = self.drzewo[wezel][0]
                    if ojciec is None:
                        tmp = szerokosc / 2
                        X_w.update({wezel:tmp})
                        return tmp

                    x_ojca = X_w[ojciec]
                    if wezel == self.drzewo[ojciec][1]:
                        tmp = x_ojca - 1
                        poprzednik = [*X_w][-1]
                        #print(poprzednik)
                        if self.glebokosci[poprzednik] > 2 and self.glebokosci[poprzednik] == self.glebokosci[wezel]:
                            #print(wezel,poprzednik,self.glebokosci[poprzednik],ojciec)
                            if poprzednik == self.drzewo[ojciec][1]:
                                if tmp < X_w[poprzednik] + 0.1:
                                    print(X_w[poprzednik])
                                    tmp = random.uniform(X_w[poprzednik] + 0.3, X_w[poprzednik] + 0.5)
                                    X_w.update({wezel: tmp})
                                    return tmp  # Dokończyć błąd z przeskakiwaniem
                                else:
                                    if tmp < X_w[poprzednik] + 0.1:
                                        print(X_w[poprzednik])
                                        tmp = random.uniform(X_w[poprzednik] + 0.3, X_w[poprzednik] + 0.5)
                                        X_w.update({wezel: tmp})
                                        return tmp
                                    else:
                                        X_w.update({wezel: tmp})
                                        return tmp
                            else:
                                if tmp < X_w[poprzednik] - 0.03:
                                    # print(X_w[poprzednik])
                                    tmp = random.uniform(X_w[poprzednik] - 0.3, X_w[poprzednik] - 0.5)
                                    X_w.update({wezel: tmp})
                                    return tmp  # Dokończyć błąd z przeskakiwaniem
                                else:

                                    X_w.update({wezel: tmp})
                                    return tmp
                        else:
                            if tmp in X_w.values():
                                tmp = random.uniform(tmp,x_ojca)
                                X_w.update({wezel:tmp})
                                return tmp
                            else:

                                X_w.update({wezel:tmp})
                                return tmp
                    elif wezel == self.drzewo[ojciec][2]:
                        tmp = x_ojca + 0.6
                        poprzednik = [*X_w][-1]
                        if self.glebokosci[poprzednik] > 2 and self.glebokosci[poprzednik] == self.glebokosci[wezel]:
                            if tmp < X_w[poprzednik]:
                                if poprzednik == self.drzewo[ojciec][1]:
                                    tmp = random.uniform(X_w[poprzednik] + 0.3, X_w[poprzednik] + 0.5)
                                    if tmp in X_w.values():
                                        tmp = random.uniform(tmp, x_ojca)
                                        X_w.update({wezel: tmp})
                                        return tmp
                                    else:
                                        X_w.update({wezel: tmp})
                                        return tmp  # Dokończyć błąd z przeskakiwaniem
                                else:
                                    tmp = random.uniform(X_w[poprzednik] + 0.3, X_w[poprzednik] + 0.5)
                                    if tmp in X_w.values():
                                        tmp = random.uniform(tmp, x_ojca)
                                        X_w.update({wezel: tmp})
                                        return tmp
                                    else:
                                        X_w.update({wezel: tmp})
                                        return tmp  # Dokończyć błąd z przeskakiwaniem
                            else:
                                X_w.update({wezel:tmp})
                                return tmp
                        else:
                            if tmp in X_w.values():
                                    tmp = random.uniform(tmp,x_ojca)
                                    X_w.update({wezel:tmp})
                                    return tmp
                            else:
                                X_w.update({wezel:tmp})
                                return tmp


        Y_w = {}
        X_data = []
        # for i in reversed(self.glebokosci):
        #     if i is None:
        #         continue
        #     else:
        #         print(i,self.glebokosci[i])
        #         X_data.append(wspolrzedne_x(i,X_wierzcholki))
        #         Y_w.update({i:wysokosc - self.glebokosci[i]})
        #         Y_wierzcholki +=[wysokosc - self.glebokosci[i]]
        for i in self.drzewo.keys():
            #print(i)
            if i is None:
                continue
            else:
                #print(i,self.drzewo[i])
                #X_data += [X_wierzcholki[i]]

                X_data.append(wspolrzedne_x(i,X_wierzcholki))
                Y_w.update({i:wysokosc - self.glebokosci[i]})
                Y_wierzcholki += [wysokosc - self.glebokosci[i]]

        self.Krawedzie(węzły[0])

        for k in self.krawedzie.items():
            for j in k[1]:
                X_krawedzie.append([X_wierzcholki[k[0]],X_wierzcholki[j]])
                Y_krawedzie.append([Y_w[k[0]],Y_w[j]])
        
        
        #print(Y_wierzcholki)
        # ustalic wysokosc dla kazdego wierzcholka dzieki temu okresli sie wysokosc kolejnego
        
        linie = go.Scatter(x = X_krawedzie,y = [4,3,4,3,3,2,3,2,3,2,3,2],mode = 'lines',connectgaps = True,
        line = dict(color='rgb(10,50,150)', width=2))
        kulki = go.Scatter(x = X_data,y = Y_wierzcholki,
        mode = 'markers+text',
        name = 'kulki',
        text = text_wierzcholkow([*X_wierzcholki]),
        marker=dict(symbol='circle-dot',
                                size=45,
                                color='#6175c1',    #'#DB4551',
                                line=dict(color='rgb(50,50,50)', width=1)
                                ))
        fig = go.Figure(data=[kulki])
        for i in range(len(X_krawedzie)):
            tmp = go.Scatter(x = X_krawedzie[i],y = Y_krawedzie[i],
            mode = 'lines',
            line = dict(color = 'rgb(10,50,150)',width = 1))
            fig.add_trace(tmp)
        fig.show()
        #fig.write_html('tmp2.html',auto_open = True)


    glebokosci = {}
    wezly = []


    def DFS(self,wezel):
        if self.drzewo[wezel]:
            print (wezel,self.kody_huffmana[wezel])
            
            self.DFS(self.drzewo[wezel][1])
            self.DFS(self.drzewo[wezel][2])
    dfs_wezly = []

    def TablicaWezlow(self,wezel): # Naprawić dziwne tworzenie węzłów
        if self.drzewo[wezel]:
            self.wezly.append(wezel)
            self.TablicaWezlow(self.drzewo[wezel][1])
            self.TablicaWezlow(self.drzewo[wezel][2])
    krawedzie = defaultdict(list)
    
    
    def Krawedzie(self,wezel): # powinno wywolac je sie dla korzenia
        if self.drzewo[wezel]:
            if self.drzewo[wezel][1] is not None:
                self.krawedzie[wezel].append(self.drzewo[wezel][1])
                self.Krawedzie(self.drzewo[wezel][1])
            if self.drzewo[wezel][2] is not None:
                self.krawedzie[wezel].append(self.drzewo[wezel][2])
                self.Krawedzie(self.drzewo[wezel][2])
            
    
    def Krawedzie_test(self):
        return dict(self.krawedzie)

    glebokosc = 0
    
    
    def Glebokosc_Wezla(self,wezel):
        if self.drzewo[wezel][0] is not None:
            self.glebokosc += 1
            self.Glebokosc_Wezla(self.drzewo[wezel][0])
        else:
            #self.glebokosc = self.glebokosc
            return self.glebokosc
            
            #print(self.glebokosc)
    def Wszystkie_Glebokosci(self,wezel):
        if self.drzewo[wezel]:
            self.Glebokosc_Wezla(wezel)
            tmp = self.ZwrocGlebokosc()
            self.glebokosci.update({wezel:tmp})
            self.Wszystkie_Glebokosci(self.drzewo[wezel][1])
            self.Wszystkie_Glebokosci(self.drzewo[wezel][2])
    def ZwrocOjca(self,wezel):
        return self.drzewo[wezel][0]
    
    def ZwrocDzieci(self,wezel):
        return {"lewy syn":self.drzewo[wezel][1],"prawy syn":self.drzewo[wezel][2]}
    def ZwrocGlebokosc(self):
        tmp = self.glebokosc
        self.glebokosc = 0
        return tmp
    def ZwrocGlebokosci(self):
        return self.glebokosci
    def ZwrocKorzen(self):
        return [*self.drzewo][0]
    def PrintDrzewo(self):
        self.DFS(self.ZwrocKorzen())
        print('-----')
        return 0
    def ZwrocKorzen(self):
        return [*self.drzewo][0]
    kody_huffmana = {}
    def OznaczanieWezla(self,wezel,tmp):
        if self.drzewo[wezel]:
            ojciec = self.drzewo[wezel][0]
            if ojciec is None:
                self.OznaczanieWezla(self.drzewo[wezel][1], tmp)
                self.OznaczanieWezla(self.drzewo[wezel][2], tmp)
            else:
                #print(wezel)
                if wezel == self.drzewo[ojciec][1]:
                    tmp += '0'
                    if wezel in self.kody_huffmana:
                        return None
                    else:
                        self.kody_huffmana.update({wezel:tmp})

                else:
                    tmp += '1'
                    if wezel in self.kody_huffmana:
                        return None
                    else:
                        self.kody_huffmana.update({wezel:tmp})
                self.OznaczanieWezla(self.drzewo[wezel][1], tmp)
                self.OznaczanieWezla(self.drzewo[wezel][2], tmp)
    def ZwrocKody(self):
        klucze_do_usuniecia = []
        for i in self.kody_huffmana.keys():
            if len(i[0]) > 1 and i[0] != 'SPACE' and i[0] != '\n':
                klucze_do_usuniecia.append(i)
        for i in klucze_do_usuniecia:
            self.kody_huffmana.pop(i)
        nowe_kody = dict()
        tmp = None
        for i in self.kody_huffmana.keys():
            tmp = i[0]
            nowe_kody.update({tmp:self.kody_huffmana[i]})
        nowe_kody.update({' ':nowe_kody['SPACE']})
        nowe_kody.pop('SPACE')
        return nowe_kody
        # elif wezel == self.drzewo[ojciec][1]:
        #     if self.kody_huffmana[wezel]:
        #         tmp = self.kody_huffmana[wezel]
        #         self.kody_huffmana.update({wezel:tmp+'0'})
        #     else:
        #         self.kody_huffmana.update({wezel:'0'})
        # elif wezel == self.drzewo[ojciec][2]:
        #     if self.kody_huffmana[wezel]:
        #         tmp = self.kody_huffmana[wezel]
        #         self.kody_huffmana.update({wezel:tmp+'1'})
        #     else:
        #         self.kody_huffmana.update({wezel:'1'})



