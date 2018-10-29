import random

from hand import Hand
from card import Card

def randy(a, b):
	return random.randint(a, b)

class Deck(object):
	def __init__(self):
		self._cards = [Card(x) for x in range(52)]
#		self.logger = logging.getLogger(__name__)
		
	@property
	def cards(self):
		return list(self._cards)
		
	
	def shuffle(self):
		for i in range(len(self._cards) - 2):
			j = randy(i, len(self._cards) -1)
			self._cards[i], self._cards[j] = self._cards[j], self._cards[i]
		return self
		
			
	def deal(self):
		if len(self._cards) != 52:
			raise CardError('incorect number of cards in deck to deal')
		hands = [Hand() for i in range(4)]
		for i in range(52):
			hands[i % 4].add(self._cards.pop(0))
		return hands
		
	def __str__(self):
		ret = ''
		for i, c in enumerate(self._cards):
			ret += str(c) + ' '
			if i % 13 == 12:
				ret += '\n'
		return ret
