import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(-50,50, 200000)
zero = np.linspace(0,0,200000)
x = lambda a: 3*a/(1+a**3)
y = lambda a: 3*a**2/(1+a**3)
plt.plot(x(t), y(t))
plt.plot(zero,t, 'g')
plt.plot(t,zero,'g')
plt.grid()
plt.show()



def binary(y):
	x=y
	con = []
	while x != 1:
		new = x//2
		con.append(str(x%2))
		x = new
	con.append('1')
	con.reverse()
	con = ''.join(con)
	return con
def denary(y):
	den = 0
	new = str(y)
	count = len(new)-1
	for i in new:
		den = den + (int(i)*2**count)
		count = count - 1
	return den
print(denary('1000010010'))
print(binary(530))

def Nimsum(lists, num = 2, check = 'stop'):
	Nimsum = []
	new = []
	x = 0
	positions = []
	for n in range(2):
		for item in lists:
			if n == 0:
				if len(item)>x:
					x = len(item)
			elif n == 1:
				count = 0
				if len(item) < x:
					diff = x-len(item)
					item1 = (diff*'0')+item
					new.append(item1)
				else:
					new.append(item)
				count = count + 1
	for i in range(x-1):
		tot = 0
		for item in new:
			if item[i] == '1':
				tot = tot + 1
		if tot%2 == 1:
			pos = i
			positions.append(pos)
			Nimsum.append('1')
		else:
			Nimsum.append('0')
	Nimsum = ''.join(Nimsum)
	if num == 2:
		return denary(Nimsum)
	else:
		return new
def Total(lists, pos):
	tot = 0
	for item in lists:
		if item[pos] == '1':
			tot = tot + 1
	tot = tot%2
	return tot
def Change(lists):
	if Nimsum(lists) > 0:
		new = lists
		for item in new:
			if item[0] == '1':
				item[0] = '0'
				
				
lists = ['11000', '10', '1011', '1111111']
x = 0
lis = Nimsum(lists, 3)
print(Nimsum(lists))	
			
