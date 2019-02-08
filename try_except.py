#FileNotFound
def fnf(s):
	try:
		f=open(s, 'r')
		print(f.read())
		f.close()
	except IOError:
		print("Sorry", s, "has not found")
#UnicodeError
def uerr(x):
	try:
		x = x.encode('ascii')
	except UnicodeError as e:
		if name == x:
			print('OK,', x)
		else:
			raise e
	return name
#KeyNotFound
def knf(x):
	try:
		return a[b]
	except:
		print("Key is not found")
if _name_=='__main__':
	print(fnf('file.log'))
	s = 'Gaёl'
	print(uerr(s))
	a={'a':0, 'b':1, 'c':2}
	print(knf('g'))
