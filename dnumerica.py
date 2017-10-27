import math
#importa las funciones matematicas

def f(x):
  return 1/x
#funcion f

def fx(x):
  return -1/ math.pow(x,2) 
#funcion fx


#Declaracion de variables
punto_inicial = 0.0
interaciones = 0.0
euler = 0.0
distancia = 0.0
err = 0.0
i = 0.0
aproximado = 0.0
exacta = 0.0


#Ingresa valores 
punto_inicial = float(raw_input("Ingrese Numero Inicial: "))
euler = float(raw_input("Ingrese Euler: "))
distancia = float(raw_input("Ingrese Distancia: "))
interaciones = int(raw_input("Ingrese Interacciones: "))


#si la distancia es 0 se muere :D
if(distancia == 0 ):
    print "Error de indeterminacion"

#Calculamos el error
err = abs( f(punto_inicial) - fx(punto_inicial))

#calcular la difenciacion 
while (distancia != 0  and (err < euler) and (i <= interaciones)):
  aproximado = (f(punto_inicial + distancia) - f(punto_inicial) / distancia)
  exacta  = fx(punto_inicial)
  err = abs(aproximado - exacta)
  i = i + 1
  distancia = distancia / 2 


if( err < euler):
  print "diferenciacion aproximada: " , aproximado


if(i < interaciones):
  print "diferenciacion aproximada: " , aproximado


"""
ALUMNOS
AUTOR : JUAN JOSE LIZCANO

RAFAEL MANJARES
CARLOS DIAZ
STEFANY PALOMAR
PEDRO PABLO PAQUE
JORGE ENRRIQUE RAMIREZ

"""
