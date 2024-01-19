import matplotlib.pyplot as plt 
import numpy as np
import math
from matplotlib import cm
from matplotlib.collections import LineCollection

#Butterfly Curve
colours = 'gykmcbr'
colours = 3*colours
for loop in range(1, 20):
	xplot = np.linspace(0,2*math.pi,200)
	yplot = np.linspace(0,2*math.pi,200)
	count = 0
	for i in (xplot):
		xplot[count] = (loop/3)*math.sin(i)*(math.exp(1)**math.cos(i)-2*math.cos(4*i)-math.sin((1/12)*i)**5)
		yplot[count] = xplot[count]/np.tan(i)
		count += 1
	plt.plot(xplot, yplot, color = colours[loop])
	
#Fermat Spiral
def Spiral(color, xcentre = 0, ycentre = 0):
	t = np.linspace(0, 24*math.pi, 400)
	r = 2*np.sqrt(t)
	yVals = r*np.sin(t)-ycentre
	xVals = r*np.cos(t)-xcentre
	xOpp =  -r*np.cos(t)-xcentre
	yOpp =  -r*np.sin(t)-ycentre
	top = plt.scatter(xVals,yVals, c = xVals, cmap = color, s = 10)
	bottom = plt.scatter(xOpp, yOpp, c = -yVals, cmap = color, s = 10)
	return top, bottom
Spiral('autumn', -40, 0)

#Circle
t = np.linspace(0, 24*math.pi, 1000)
x = np.sin(t) -15
y = np.cos(t) 
#plt.plot(x,y, color = 'c')

plt.title( 'Computer Art' ) 
plt.gca().set_aspect('equal')
plt.show()

#linestyle = 'ls', dotted = ':', dashed == '--', linewidth = 'lw'
#label axes: plt.xlabel(''), plt.ylabel('')
#location of title: use 'loc = "" '
#grid() takes x,y default is both, but you can choose.
#subplot() takes 'row', 'column', 'plot num' - 'suptitle("")' gives the title of the whole subplot
#colour map (aka cmap) takes digits from 0 to 100 - color is also abbreviated to 'c' - size of dot can be changed with 's'
#can set transparency using 'alpha'
