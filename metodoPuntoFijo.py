"""
from f import f 

x = float(raw_input("Ingrese X inicial: "))
max_iter = float(raw_input("Ingrese Max Iteraciones: "))
#error = 0.001 
error = float(raw_input("Ingrese Valor Tolerado: "))
i = 0
print "\n i \t\t\t x \t \t error \n"
print "-----------------------------------------------------------------------------------"


while i < max_iter:
  a = x 
  x = f(a)
  e = ( abs(x) - abs(a) )
  #e = abs(x - a) 
  print " %.0f \t\t %.3f  \t %.3f  \n" %(i , x , e)

  if(e < error):
    i = max_iter +1 
  i+= 1


print "La aproximacion es %d con un error de : %d \n" % (i , e)

"""

horas_trabajadas = 0
tarifa = 0
h_extras = 0
salario = 0
tarifa_extra = 0

horas_trabajadas = int(raw_input("Ingrese horas trabajadas: "))
tarifa = int(raw_input("Ingrese tarifa: "))


if(horas_trabajadas <= 40):
  salario = horas_trabajadas * tarifa
else:
  tarifa_extra = tarifa + 0.50 * tarifa
  h_extras = horas_trabajadas - 40
  salario = h_extras * tarifa_extra + 40 * tarifa


print "El salario es: ", salario


