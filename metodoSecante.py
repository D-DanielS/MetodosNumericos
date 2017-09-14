from f import f

def sec(a,b,tol,it_max):
  cont = 0
  c = (a+b)/2
  while(abs(f(c))>tol and cont < it_max):
     c = b - ( (b-a) / ( f(b) - f(a) ) ) * f(b) 
     a = b
     b = c
     cont += 1
     print "Interaciones" , cont

  return c
impr = sec(4,0,0.001, 40)
print impr
