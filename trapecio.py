import math
import numpy as np


def f(x):
    y = pow(x,2)
    return y

lim_sup = float(input('Limite Superior: '))
lim_inf = float(input('Limite Inferior: '))
n_trap = int(input('Ingrese Numero de Trapecios: '))

x = np.zeros([n_trap + 1]) 
h = (lim_sup -  lim_inf ) / n_trap
x[0] = lim_inf
x[n_trap] = lim_sup
suma = 0


for i in np.arange(1,n_trap):
  x[i] = x[i-1] +h
  suma = suma + f(x[i])

integral = (h/2) *( f(x[0] ) + 2 * suma + f(x[n_trap]) )
print "Resultado de la integral es: ", integral
