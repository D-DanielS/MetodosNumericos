from f import f

x1 = float(raw_input('Introduce el valor de inicio x1: '))
x0 = float(raw_input('Introduce el valor de inicio x0: '))
erroru=float(raw_input('Introduce el error: '))
raiz=[]
raiz.insert(0,0)
i = 0 
error = 1
while abs(error) > erroru:
    x2 = x1 - ( f(x1) * (x1-x0) ) / ( f(x1) - f(x0) )
    raiz.append(x2)
    x0 = x1
    x1 = x2
    i += 1 
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print "interaciones: " , i
print "Raiz: ", x2