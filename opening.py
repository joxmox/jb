from bid import Bid
from reply import *

class Opening(object):
    pass
    

class o1Maj5(Opening):
    name = 'Five card major'
    reply = [rMaj5Stenb, rMaj5Limit, rOneOverOne, rOneNT]

    @classmethod
    def check(cls, hand):
        if not hand.has_maj5():
            return None
        if hand.hcp < 10 or hand.hcp > 21:
            return None
        if hand.length() + hand.length(1) + hand.hcp < 20:
            return None
        return Bid(0, hand.best_major(), cls)
    
        
class o1MinBest(Opening):
    name = 'Best minor'
    reply = [rOneOverOne, rMinBestLim]        

    @classmethod
    def check(cls, hand):
        if hand.hcp < 10 or hand.hcp > 21:
            return None
        if hand.length() + hand.length(1) + hand.hcp < 20:
            return None    
        return Bid(0, hand.best_minor(), cls)
        
class o1NT(Opening):
    name = 'One no trump'
        
    @classmethod
    def check(cls, hand):
        if hand.hcp < 15 or hand.hcp > 17:
            return None
        if not hand.is_balanced():
            return None
        return Bid.parse('1nt', cls)

class o2NT(Opening):
    name = 'Two no trump'
        
    @classmethod
    def check(cls, hand):
        if hand.hcp < 20 or hand.hcp > 21:
            return None
        if not hand.is_balanced() and not hand.is_marmic():
            return None
        return Bid.parse('2nt', cls)

class o2MajWeak(Opening):
    name = "Weak two major"

    @classmethod
    def check(cls, hand):
        if hand.in_zone() and hand.hcp >= 10:
            if hand.sut_length(3) == 6 and hand.sut_qual(3) >= 6:
                return Bid(1, 3, cls)
            if hand.sut_length(2) == 6 and hand.sut_qual(2) >= 6:
                return Bid(1, 2, cls)
            return None
        elif not hand.in_zone():
            if hand.hcp > 10:
                if hand.sut_length(3) == 6:
                    return Bid(1, 3, cls)
                elif hand.sut_length(2) == 6:
                    return Bid(1, 2, cls)
                else:
                    return None
            elif hand.hcp > 8:
                if hand.sut_length(3) == 6 and hand.sut_qual(3) >= 6:
                    return Bid(1, 3, cls)
                if hand.sut_length(2) == 6 and hand.sut_qual(2) >= 6:
                    return Bid(1, 2, cls)
                return None
            else:
                return None
        else:
            return None

class o2DiaWeak(Opening):
    name = "Weak two diamonds"
    reply = [

    @classmethod
    def check(cls, hand):
        if hand.in_zone() and hand.hcp >= 10:
            if hand.sut_length(1) == 6 and hand.sut_qual(1) >= 6:
                return Bid(1, 1, cls)
            return None
        elif not hand.in_zone() and hand.hcp >= 8:
            if hand.sut_length(1) == 6:
                return Bid.parse('2d', cls)
            else:
                return None
        else:
            return None
    
class o2CluStrong(Opening):
    name = "Two clubs"
    
    @classmethod
    def check(cls, hand):
        if hand.hcp < 22:
            return None
        else:
            return Bid.parse('2c', cls)
        
        
        

def main():
    pass

if __name__ == '__main__':
    main()

    
