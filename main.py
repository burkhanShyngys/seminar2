from mybox import myBox
from myclass import Calculator

box = myBox()
box.add(Calculator(5, '+', 6))
box.add(Calculator(12, '-', 4))
box.add(Calculator(3, '*', 5))
box.add(Calculator(6, '/', 4))

box.remove(2)
for i in box:
	i.print_ans()
