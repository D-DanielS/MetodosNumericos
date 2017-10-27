
import random

"""
n = int(input("Ingrese n: "))

arr__uno = [None] * n
arr__dos = [None] * n
suma__arr = [None] * n



for i in range(0,n):
  arr__uno[i] = random.randint(1,100)
  arr__dos[i] = random.randint(1,100)

print "arrUno = " , arr__uno
print "arrDos = " , arr__dos

for i in range(0,n):
  suma__arr[i] = arr__uno[i] + arr__dos[i] 

print "Suma de Vectores"
print suma__arr
"""

print("SUMA DE MATRICES")
col = int(input("Numero de Columnas: "))
row = int(input("Numero de Filas: "))

matriz1 = [[0 for x in range(row)] for y in range(col)]
matriz2 = [[0 for x in range(row)] for y in range(col)]
matriz3 = [[0 for x in range(row)] for y in range(col)]

for i in range(row):
  for j in range(col):
    matriz1[i][j] = random.randint(1,100)

for i in range(row):
  for j in range(col):
    matriz2[i][j] = random.randint(1, 100)

print "matriz 1"
print matriz1
print "\n"

print "matriz 2"
print matriz2
print "\n"

for i in range(row):
  for j in range(col):
    matriz3[i][j] = matriz1[i][j] + matriz2[i][j]

print "\n"
print("Suma de las matrices")
print(matriz3)
