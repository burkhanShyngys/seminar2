class Calculator:
	def __init__(self, x, y, c):
		self.x=x
		self.y=y
		self.c=c
	def print_ans(self):
		if self.y=='+':		
			print(self.x+self.c)
		elif self.y=='-':
			print(self.x-self.c)
		elif self.y=='*':
			print(self.x*self.c)
		elif self.y=='/':
			print(self.x/self.c)
	def defaultVal(self):
		self.x=5
		self.c=2
		self.y='+'
