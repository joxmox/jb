from deck import Deck
from opening import *

class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.hands = self.deck.deal()
        for h in self.hands:
            h.analyze()
        self.state = 0 # view deal info
        self.id = 0

    def set_id(self, id):
        self.id = id
        return self

class Games(object):

    nextid = 1

    def __init__(self):
        self.games = {}

    def new(self):
        id = Games.nextid
        print "new", id
        Games.nextid += 1
        self.games[id] = Game().set_id(id)
        return {
            'id' : id,
        }

    def next(self, id):
        id = int(id)
        print "id", id
        game = self.games[id]
        state = game.state
        print "state", state
        if state == 0:
            return self.send_deal_info(game)
        elif state == 1:
            return self.send_hand(game)


    def send_deal_info(self, game):
        print "deal_info"
        self.state = 1
        data= {
            'id' : game.id,
            'action' : 'deal_info',
        }
        print data
        return data

    def send_hand(self, game):
        print self.hands
        return {
            'id' : game.id,
            'action' : 'view_hand',
            'hand' : game.hand[0],
        }
