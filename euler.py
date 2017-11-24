import math
import numpy as np

def dydx(x, y):
    return y*np.sqrt(x) 
   

n = 1050 #intervalos
x0 = 0.0
xf = 2.0
y0 = 1  #punto inicial

h = (xf - x0) / n



x = [x0]
y = [y0]

for i in range(n):
  y0 = y0 + h * dydx( x0 , y0)
  y.append(y0)
  x0 = x0 + h
  x.append(x0)


print (x)
print (y) 







