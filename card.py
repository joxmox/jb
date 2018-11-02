class CardError(Exception):
    pass

class Card(object):

    values = '23456789TJQKA'
    suits = 'cdhs'

    def __init__(self, data):
        if not str(data).isdigit() or data < 0 or data > 51:
            raise CardError('invalid input to card generation')
        self._data = data
        self._num = self._data % 13
        self._val = Card.values[self._num]
        self._sut = self._data // 13
        self._sym = Card.suits[self._sut]
        self._crd = self._val + self._sym
        

    @staticmethod
    def from_str(txt):
        val, sym = list(txt)
        num = '23456789TJQKA'.index(val)
        data = Card.suits.index(sym) * 13 + num
        return Card(data)
        

    @property
    def data(self):
        return self._data

    @property
    def num(self):
        return self._num
    
    @property
    def val(self):
        return self._val
        
    @property
    def sut(self):
        return self._sut

    @property
    def sym(self):
        return self._sym

    @property
    def crd(self):
        return self._crd

    def __gt__(self, other):
        return self._sut > other._sut or (self._sut == other._sut and self._num > other._num)
        
    def __le__(self, other):
        return self._sut < other._sut or (self._sut == other._sut and self._num <= other._num)

    def __str__(self):
        return self.crd
