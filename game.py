import time

from deck import Deck
from opening import *
from bid import Bid

class Game(object):

    def __init__(self, dealer, zone):
        self.deck = Deck()
        self.deck.shuffle()
        self.hands = self.deck.deal()
        for h in self.hands:
            h.analyze()
        self.state = 'deal_info'
        self.id = 0
        self.passcnt = 0
        self.opened = False
        self.dealer = dealer
        self.bidder = dealer

    def set_id(self, id):
        self.id = id
        return self

class Games(object):

    nextid = 1

    def __init__(self):
        self.games = {}
        self.funcmap = {
            'deal_info' : self.deal_info,
            'my_hand' : self.my_hand,
            'part_hand' : self.part_hand,
            'end_game' : self.end_game,
            'do_bid' : self.do_bid,
        }

    def new(self):
        id = Games.nextid
        print "new", id
        Games.nextid += 1
        self.games[id] = Game(0, None).set_id(id)
        game = self.games[id]
        return {
            'id' : id,
        }

    def next(self, id):
        id = int(id)
        print "id", id
        game = self.games[id]
        state = game.state
        if state not in self.funcmap:
            state = 'end_game'
        print "state", state
        func = self.funcmap[state]
        return func(game, state)

    def deal_info(self, game, state):
        print "deal_info"
        data = {
            'id' : game.id,
            'action' : state,
            'info' : {
                'id' : game.id,
                'dealer' : ['South', 'West', 'North', 'East'][game.dealer],
                'zone' : 'None',
            },
        }
        game.state = 'my_hand'
        return data

    def my_hand(self, game, state):
        hand = game.hands[0]
        data = {
            'id' : game.id,
            'action' : state,
            'hand' : {
                'cards' : str(hand),
                'hcp' : hand.hcp,
            },
        }
        game.state = 'part_hand';
        return data

    def part_hand(self, game, state):
        hand = game.hands[2]
        data = {
            'id' : game.id,
            'action' : state,
            'hand' : {
                'cards' : str(hand),
                'hcp' : hand.hcp,
            },
        }
        game.state = 'do_bid';
        return data

    def do_bid(self, game, state):
        time.sleep(1)
        hand = game.hands[game.bidder]
        if game.bidder == 0 or game.bidder == 2:
            bid = hand.try_open()
        else:
            bid = {
                'name' : 'Pass',
                'symb' : 'Pass',
                'color' : 'blk',
                'text' : 'Pass',
            }
        if bid['name'] == 'Pass':
            game.passcnt += 1
        else:
            game.passcnt = 1
        data = {
            'id' : game.id,
            'action' : state,
            'bid' : bid,
            'bidder' : 'swne'[game.bidder]
        }
        game.bidder = (game.bidder + 1) % 4
        if game.passcnt == 4:
            game.state = 'end_game';
        return data
        

    def end_game(self, game, state):
        data = {
            'id' : game.id,
            'action' : state,
        }
        game.state = '';
        return data
