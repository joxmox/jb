import time
import random

from deck import Deck
from opening import *
from bid import Bid

class Game(object):

    def __init__(self, id, num, dealer, zone):
        self.deck = Deck(num)
        self.num = self.deck.num
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
        self.bids = []


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
        try:
            num = int(data.get('num', 0))
        except ValueError:
            num = 0
        Games.nextid += 1
        self.games[id] = Game(id, num, 0, None)
        game = self.games[id]
        game.id = id
        return {
            'id' : id,
            'num' : game.num,
        }

    def next(self, id):
        id = int(id)
        game = self.games[id]
        state = game.state
        if state not in self.funcmap:
            state = 'end_game'
        func = self.funcmap[state]
        return func(game, state)

    def deal_info(self, game, state):
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
                'suited' : hand.by_suit(),
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
                'suited' : hand.by_suit(),
                'hcp' : hand.hcp,
            },
        }
        game.state = 'do_bid';
        return data

    def do_bid(self, game, state):
        time.sleep(1)
        hand = game.hands[game.bidder]
        if game.bidder == 0 or game.bidder == 2:
            if game.opened:
                bid, sut, cls = game.bids[-2]
                bid, sut, cls = hand.reply(sut, cls)
                
            else:
                bid, sut, cls  = hand.try_open()
                if bid['name'] != 'Pass':
                    game.opened = True
        else:
            bid = {
                'name' : 'Pass',
                'symb' : 'Pass',
                'color' : 'blk',
                'text' : 'Pass',
            }
            sut = None
            cls = None
        game.bids.append([bid, sut, cls])
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
