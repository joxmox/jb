from bid import Bid

class Reply(object):
    pass

class rMaj5Stenb(Reply):
    name = 'Stenberg 2NT (GF)'
    @classmethod
    def check(cls, hand, sut):
        if hand.sut_length(sut) >= 4 and hand.stp(sut) >= 12:
            return Bid.parse('2nt', cls)
        else:
            return None

class rMaj5Limit(Reply):
    name = 'Limit raise'
    @classmethod
    def check(cls, hand, sut):
        if hand.sut_length(sut) >= 3:
            if hand.stp(sut) >= 9:
                return Bid(2, sut)
            elif hand.stp(sut) >= 6:
                return Bid(1, sut, cls)
            else:
                return None
        else:
            return None

class rMinBestLim(Reply):
    name = "Limit raise"
    @classmethod
    def check(cls, hand, sut):
        if hand.sut_length(sut) >= 3:
            if hand.stp(sut) >= 9:
                return Bid(2, sut)
            elif hand.stp(sut) >= 6:
                return Bid(1, sut, cls)
            else:
                return None
        else:
            return None

class rOneOverOne(Reply):
    name = "One over one"
    @classmethod
    def check(cls, hand, sut):
        if hand.hcp >= 6:
            if sut == 0 or sut == 1:
                if hand.has_maj4:
                    return Bid(0, hand.best_major(), cls)
                elif sut == 0 and hand.sut_length(1) >= 4:
                    return Bid(0, 1, cls)
                else:
                    return None
            elif sut == 2 and hand.sut_length(2) >= 4:
                return Bid(0, 3, cls)
            else:
                return None
        else:
            return None
                    

class rTwoOverOne(Reply):
    name = "Two over One (GF)"
    @classmethod
    def check(cls, hand, sut):
        return None
    

class rOneNT:
    name = "Weak 1NT reaponse"
    @classmethod
    def check(cls, hand, sut):
        return None




class rMinBest2NT(Reply):
    name = "Invititation 3NT"
    @classmethod
    def check(cls, hand, sut):
        return None


