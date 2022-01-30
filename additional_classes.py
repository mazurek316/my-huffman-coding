class HuffmanList:
    def __init__(self,data,nast = None,poprzedni = None):
        self.freq = data
        self.next = nast
        self.previous = poprzedni



class DataRec:
    def __init__(self,supersymbol = 0,runLength = 0,frequency = 0):
        self.symbol = supersymbol
        self.runLen = runLength
        self.freq = frequency
    def __eq__(self, other):
        if self.symbol == ' ' and other.symbol == ' ':
            return True
        return self.symbol == other.symbol and self.runLen == other.runLen
    def __lt__(self, other):
        return self.freq < other.freq