import math
import numpy as np

def dydx(x, y):
    return y*np.sqrt(x) 
   
#intervalos
n = int(input('Ingrese Numero de Intervalos: '))
x0 = float(input('Ingrese Numero x0: '))
xf = float(input('Ingrese Numero xf: '))
y0 = 1  #punto inicial

#Consiste en dividir los intervalos que va de (x0) a (xf)  en (n)  subintervalos de ancho (h) osea: 
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







