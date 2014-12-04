class Fraction:
	def __init__(self, top, bottom):
		assert isinstance(top, int)
		assert isinstance(bottom, int)
		self.top = top
		self.bottom = bottom
		
	def __str__(self):
		return str(self.top)+'/'+str(self.bottom)
		
	def __add__(self, other):
		# handle <int> type
		if isinstance(other, int):
			other = Fraction(other, 1)
		#assert isinstance(other_frac, Fraction)
		top = self.top*other.bottom + self.bottom*other.top
		if top == 0:
			return 0
		bottom = self.bottom*other.bottom
		common = Fraction._max_common_divisor(top, bottom)
		return Fraction(top/common,bottom/common)
	
	def __radd__(self, other_frac):
		"""if one cannot add with this frac, use __radd__"""
		print 'using __radd__'
		return self + other_frac
	
	def __sub__(self, other_frac):
		assert isinstance(other_frac, Fraction)
		top = self.top*other_frac.bottom - self.bottom*other_frac.top
		if top == 0:
			return 0
		bottom = self.bottom*other_frac.bottom
		common = Fraction._max_common_divisor(top, bottom)
		return Fraction(top/common,bottom/common)
			
	def __eq__(self, other_frac):
		assert isinstance(other_frac, Fraction)
		return self.bottom*other_frac.top == self.top*other_frac.bottom
		
		
	@classmethod
	def _max_common_divisor(cls, m, n):
		m, n = max(m, n), min(m,n)
		while m%n:
			m, n = n, m%n
		return n
		
if __name__ == '__main__':
	f1 = Fraction(2,5)
	f2 = Fraction(3,7)
	print f1
	print f2
	#print f1+f2
	print f1 == f2
	print f1-f2
	print f1+f2
	print 2+f1
