from f import f

def bis(a,b,tol,it_max):
  if(a>b):
    return bis(b,a,tol,it_max)  
  cont = 0
  c = (a+b)/2
  while(abs(f(c))>tol and cont < it_max):
    if(f(a) * f(c) < 0):
      b = c
    if(f(c) * f(b) < 0):
      a = c
    c = (a+b)/2
    cont += 1
    print "Interaciones" , cont
  return c

imprimir = bis(4,0,0.001, 1000)
print imprimir
