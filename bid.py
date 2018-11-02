class Bid(object):

# sut = c,d,h,s,nt,x
# for x, val = pass,x,xx
# other, val = 1,2,3,4,5,6,7

    @staticmethod
    def parse(txt, cls=None):
        txt = txt.lower()
        try:
            if txt == 'x':
                return Bid(1, 5, cls)
            elif txt == 'xx':
                return Bid(2, 5, cls)
            elif txt[0] == 'p':
                return Bid(0, 5, cls)
            else:
                val = int(txt[0])
                sym = 'cdhsn'.index(txt[1])
                if val < 1 or val > 7:
                    return Bid(3, 5, cls)
                return Bid(val - 1, sym, cls)
        except Exception:
            return Bid(3, 5, cls)

    def __init__(self, val, sut, cls=None):
        if cls is not None:
            print cls
        self._val = val
        self._sut = sut
        self._cls = cls
        if sut == 0:
            self._col = 'grn'
        elif sut == 1:
            self._col = 'yel'
        elif sut == 2:
            self._col = 'red'
        else:
            self._col = 'blk'

    def __str__(self):
        val = self._val
        sut = self._sut
        if sut == 5:
            if val == 0:
                return 'Pass'
            elif val == 1:
                return 'X'
            elif val == 2:
                return 'XX'
            else:
                return '?'
        else:
            return str(val + 1) + 'cdhsn'[sut]

    @property
    def cls(self):
        return self._cls

    @property
    def val(self):
        return self._val

    @property
    def sut(self):
        return self._sut

    @property
    def str(self):
        return str(self)

    @property
    def col(self):
        return self._col

    @property
    def sym(self):
        val = self._val
        sut = self._sut
        if sut == 5:
            if val == 0:
                return 'Pass'
            elif val == 1:
                return 'X'
            elif val == 2:
                return 'XX'
            else:
                return '?'
        else:
            return str(val + 1) + ['&#x2663', '&#x2666', '&#x2665', '&#x2660'][sut]

    def sutsym(self):
        return 'cdhsn'[self._sut]


