from bid import Bid

class Opening(object):
    pass
    

class o1Maj5(Opening):
    name = 'Five card major'
    def __init__(self, suite):
        pass
    
    @staticmethod
    def check(hand):
        if not hand.has_maj5():
            return None
        if hand.hcp < 10 or hand.hcp > 21:
            return None
        if hand.length() + hand.length(1) + hand.hcp < 20:
            return None
        return Bid(0, hand.best_major())
        
class o1MinBest(Opening):
    name = 'Best minor'
    def __init__(self, suite):
        pass
        
    @staticmethod
    def check(hand):
        if hand.hcp < 10 or hand.hcp > 21:
            return None
        if hand.length() + hand.length(1) + hand.hcp < 20:
            return None    
        return Bid(0, hand.best_minor())
        
class o1NT(Opening):
    name = 'One no trump'
    def __init__(self):
        pass
        
    @staticmethod
    def check(hand):
        if hand.hcp < 15 or hand.hcp > 17:
            return None
        if not hand.is_balanced():
            return None
        return Bid.parse('1nt')

class o2NT(Opening):
    name = 'Two no trump'
    def __init__(self):
        pass
        
    @staticmethod
    def check(hand):
        if hand.hcp < 20 or hand.hcp > 21:
            return None
        if not hand.is_balanced() and not hand.is_marmic():
            return None
        return Bid.parse('2nt')

class o2MajWeak(Opening):
    name = "Weak two major"
    def __init__(self):
        pass
    @staticmethod
    def check(hand):
        if hand.in_zone() and hand.hcp >= 10:
            if hand.sut_length(3) == 6 and hand.sut_qual(3) >= 6:
                return Bid(1, 3)
            if hand.sut_length(2) == 6 and hand.sut_qual(2) >= 6:
                return Bid(1, 2)
            return None
        elif not hand.in_zone():
            if hand.hcp > 10:
                if hand.sut_length(3) == 6:
                    return Bid(1, 3)
                elif hand.sut_length(2) == 6:
                    return Bid(1, 2)
                else:
                    return None
            elif hand.hcp > 8:
                if hand.sut_length(3) == 6 and hand.sut_qual(3) >= 6:
                    return Bid(1, 3)
                if hand.sut_length(2) == 6 and hand.sut_qual(2) >= 6:
                    return Bid(1, 2)
                return None
            else:
                return None
        else:
            return None

class o2DiaWeak(Opening):
    name = "Weak two diamonds"
    def __init__(self):
        pass
    @staticmethod
    def check(hand):
        if hand.in_zone() and hand.hcp >= 10:
            if hand.sut_length(1) == 6 and hand.sut_qual(1) >= 6:
                return Bid(1, 1)
            return None
        elif not hand.in_zone() and hand.hcp >= 8:
            if hand.sut_length(1) == 6:
                return Bid.parse('2d')
            else:
                return None
        else:
            return None
    
class o2CluStrong(Opening):
    name = "Two clubs"
    def __init__(self):
        pass
    
    @staticmethod
    def check(hand):
        if hand.hcp < 22:
            return None
        else:
            return Bid.parse('2c')
        
        
        
