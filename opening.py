class Opening(object):
	pass
	

class five_major(Opening):
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
		return hand.best_major()
		
class best_minor(Opening):
	name = 'Best minor'
	def __init__(self, suite):
		pass
		
	@staticmethod
	def check(hand):
		if hand.hcp < 10 or hand.hcp > 21:
			return None
		if hand.length() + hand.length(1) + hand.hcp < 20:
			return None	
		return hand.best_minor()
		
class one_nt(Opening):
	name = 'One no trump'
	def __init__(self):
		pass
		
	@staticmethod
	def check(hand):
		if hand.hcp < 15 or hand.hcp > 17:
			return None
		if not hand.is_balanced():
			return None
		return True

class two_nt(Opening):
	name = 'Two no trump'
	def __init__(self):
		pass
		
	@staticmethod
	def check(hand):
		if hand.hcp < 20 or hand.hcp > 21:
			return None
		if not hand.is_balanced() and not hand.is_marmic():
			return None
		return True

class two_major_weak(Opening):
	name = "Weak two major"
	def __init__(self):
		pass
	@staticmethod
	def check(hand):
		if hand.in_zone() and hand.hcp >= 10:
			if hand.sut_length(3) == 6 and hand.sut_qual(3) >= 6:
				return 3
			if hand.sut_length(2) == 6 and hand.sut_qual(2) >= 6:
				return 2
			return None
		elif not hand.in_zone():
			if hand.hcp > 10:
				if hand.sut_length(3) == 6:
					return 3
				elif hand.sut_length(2) == 6:
					return 2
				else:
					return None
			elif hand.hcp > 8:
				if hand.sut_length(3) == 6 and hand.sut_qual(3) >= 6:
					return 3
				if hand.sut_length(2) == 6 and hand.sut_qual(2) >= 6:
					return 2
				return None
			else:
				return None
		else:
			return None

class two_diamonds_weak(Opening):
	name = "Weak two diamonds"
	def __init__(self):
		pass
	@staticmethod
	def check(hand):
		if hand.in_zone() and hand.hcp >= 10:
			if hand.sut_length(1) == 6 and hand.sut_qual(1) >= 6:
				return 1
			return None
		elif not hand.in_zone() and hand.hcp >= 8:
			if hand.sut_length(1) == 6:
				return 1
			else:
				return None
		else:
			return None
	
class two_clubs_strong(Opening):
	name = "Two clubs"
	def __init__(self):
		pass
	
	@staticmethod
	def check(hand):
		if hand.hcp < 22:
			return None
		else:
			return True
		
		
		
