import random


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
