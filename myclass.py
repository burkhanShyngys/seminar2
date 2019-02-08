class Calculator:
	def __init__(self, x, y, c):
		self.x=x
		self.y=y
		self.c=c
	def print_ans(self):
		if self.c=='+':		
			print(self.x+self.y)
		elif self.c=='-':
			print(self.x-self.y)
		elif self.c=='*':
			print(self.x*self.y)
		elif self.c=='/':
			print(self.x/self.y)
	def defaultVal(self):
		self.x=5
		self.y=2
		self.c='+'
