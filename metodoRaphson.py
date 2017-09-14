from f import f

def deri(x):
    d = (2*x)-3
    return (d)



x = float(raw_input('Introduce el valor de inicio: '))
erroru = float(raw_input('Introduce el error: '))
raiz=[]
raiz.insert(0,0)
i=0
error = 1
while abs(error) > erroru:
    x1=x-(f(x) / deri(x))
    raiz.append(x1)
    i+= 1
    x = x1
    error=(raiz[i]-raiz[i-1])/raiz[i]
    print "iteraciones: ", i
print "Raiz: ", x
