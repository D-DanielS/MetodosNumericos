from f import f 

x = float(raw_input("Ingrese X inicial: "))
max_iter = float(raw_input("Ingrese Max Iteraciones: "))
#error = 0.001 
error = float(raw_input("Ingrese Valor Tolerado: "))
i = 0
print "\n i \t\t\t x \t \t error \n"
print "-----------------------------------------------------------------------------------"


while (i < max_iter):
  a = x 
  x = f(a)
  e = ( abs(x) - abs(a) )
  print " %.0f \t\t %.3f  \t %.3f  \n" %(i , x , e)

  if(e < error):
    i = max_iter +1 
  i+= 1


print "La aproximacion es %d con un error de : %.1d \n" % (i , e)

