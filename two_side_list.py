class HuffmanList:
    def __init__(self,data,nast = None,poprzedni = None):
        self.freq = data
        self.next = nast
        self.previous = poprzedni