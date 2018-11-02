from opening import *

class Hand(object):
    def __init__(self):
        self.cards =  []
        self._hcp = None
        self.open_seq = [o2CluStrong, o2NT, o1Maj5, o1MinBest, o2MajWeak, o2DiaWeak]

    def add(self, card):
        self.cards.append(card)
        self.cards.sort()
        
    def sorted(self):
        return sorted(self.cards)
        
    def analyze(self):
        self._hcp = sum([max(c.val-8, 0) for c in self.cards])
        self._length = [sum(1 for crd in self.cards if crd.sut == sut) for sut in range(4)]
        for sut in range(4):
            print sut, sum(1 for crd in self.cards if crd.sut == sut)
        
    @property    
    def hcp(self):
        return self._hcp
        
    def in_zone(self):
        return False
        
    def is_balanced(self):
        if min(self._length) > 1 and self._length.count(2) <= 1:
            return True
        else:
            return False
            
    def is_marmic(self):
        return sorted(self._length) == [1, 4, 4, 4]
    
    def has_maj5(self):
        return max(self._length[2:]) >= 5
        
    def length(self, ind=0):
        return sorted(self._length, reverse=True)[ind]
        
    def sut_length(self, sut):
        return self._length[sut]
        
    def sut_qual(self, sut):
        return 7
    
    def best_major(self):
        if self._length[2] > self._length[3]:
            return 2
        else:
            return 3
            
    def best_minor(self):
        if self._length[0] > self._length[1]:
            return 0
        elif self._length[0] == 3 and self._length[1] == 3:
            return 0
        else:
            return 1


    def try_open(self):
        for o in self.open_seq:
            bid = o.check(self)
            name = o.name
            if bid:
                break
        if not bid:
            bid = Bid.parse('pass')
            name = 'Pass'
        data = {
            'name' : bid.str,
            'symb' : bid.sym,
            'color' : bid.col,
            'text' : name,
        }
        return data

    def str_by_suit(self):
        res = {}
        for sut, sym in zip(range(4), ['c', 'd', 'h', 's']):
            res[sym] = [self.fixval(c.val) for c in sorted(self.cards, reverse=True) if c.sut==sut]
        return res

    def fixval(self, num):
        if num < 8:
            return str(num + 2)
        else:
            return 'TJQKA'[num - 8];


    def __str__(self):
        return ' '.join([str(c) for c in self.cards])

    def pretty(self):
        print [str(c) for c in self.sorted()]
        print [str(c) for c in reversed(self.sorted())]
        ret = ''
        for sut in reversed(range(4)):
            ret += ''.join(c.valsym() if c.sut == sut else '' for c in reversed(self.sorted())) + '\n'
        return ret

def main():
    from deck import Deck
    d = Deck().shuffle()
    print d
    g = d.deal()
    print
    for f in g:
        print f
    print
    h = g[0]
    print h
    print
    print h.str_by_suit()


if __name__ == '__main__':
    main()
