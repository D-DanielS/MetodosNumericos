import math

def f(x):
  return 1/x


def fx(x):
  return -1/ math.pow(x,2) 


punto_inicial = 0.0
interaciones = 0.0
euler = 0.0
distancia = 0.0
err = 0.0
i = 0.0
aproximado = 0.0
exacta = 0.0

punto_inicial = float(raw_input("Ingrese Numero Inicial: "))
euler = float(raw_input("Ingrese Euler: "))
distancia = float(raw_input("Ingrese Distancia: "))
interaciones = int(raw_input("Ingrese Interacciones: "))


if(distancia == 0 ):
    print "Error de indeterminacion"


err = abs( f(punto_inicial) - fx(punto_inicial))

while (distancia != 0  and (err < euler) and (i <= interaciones)):
  aproximado = (f(punto_inicial + distancia) - f(punto_inicial) / distancia)
  exacta  = fx(punto_inicial)
  err = abs(aproximado - exacta)
  i = i + 1
  distancia = distancia / 2 

if( err < euler):
  print "diferenciacion aproximada: " , aproximado

if(i <= interaciones):
  print "diferenciacion aproximada: " , aproximado



