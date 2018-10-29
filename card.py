class CardError(Exception):
	pass
class CardError(Exception):
	pass

class Card(object):
	def __init__(self, num):
		if not str(num).isdigit() or num < 0 or num > 51:
			raise CardError('invalid input to card generation')
		self._num = num
		self._val = self._num % 13
		self._sut = self._num // 13
		
	def get_num(self):
		return self._num
		
	def get_val(self):
		return self._val
	
	def _set_card(self, num):
		raise CardError('cannot resassign card value')
		
	@property
	def num(self):
		return self._num
	
	@property
	def val(self):
		return self._val
		
	@property
	def sut(self):
		return self._sut
		
	def valsym(self):
		return '23456789TJQKA'[self._val]
		
	def __gt__(self, other):
		return self._num > other._num
		
	def __ge__(self, other):
		return self._num >= other._num

	def __str__(self):
		v = '23456789TJQKA'[self._val]
		c = 'cdhs'[self._sut]
		return v + c
