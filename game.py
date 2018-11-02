import time
import random

from deck import Deck
from opening import *
from bid import Bid

class Game(object):

    def __init__(self, id, num, dealer, zone):
        if num == 0:
            num = random.randint(1, 100000)
        self.num = num
        self.deck = Deck(num)
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


class Games(object):

    nextid = 1

    def __init__(self):
        self.games = {}
        self.funcmap = {
            'deal_info' : self.deal_info,
            'show_hands' : self.show_hands,
            'part_hand' : self.part_hand,
            'end_game' : self.end_game,
            'do_bid' : self.do_bid,
        }

    def new(self, data):
        id = Games.nextid
        print "new", id
        try:
            num = int(data['num'])
        except ValueError:
            num = 0
        print "num", num
        Games.nextid += 1
        self.games[id] = Game(id, num, 0, None)
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
                'num' : game.num,
                'dealer' : ['South', 'West', 'North', 'East'][game.dealer],
                'zone' : 'None',
            },
        }
        game.state = 'show_hands'
        return data

    def show_hands(self, game, state):
        hand = game.hands[0]
        cards = {}
        for a, b in zip(range(4), ['south','west','north','east']):
            hand = game.hands[a]
            cards[b] = {
                'cards' : str(hand),
                'suited' : hand.str_by_suit(),
                'hcp' : hand.hcp,
            }
        data = {
            'id' : game.id,
            'action' : state,
            'hands' : cards,
        }
        game.state = 'do_bid';
        return data

    def part_hand(self, game, state):
        hand = game.hands[2]
        data = {
            'id' : game.id,
            'action' : state,
            'hand' : {
                'cards' : str(hand),
                'suited' : hand.str_by_suit(),
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
