from f import f

xi = float(raw_input("Ingrese xi: "))
xs = float(raw_input("Ingrese xs: "))
error = float(raw_input("Ingrese error: "))

xa = (xi + xs)/2.0
i = 0
itmax = 100

print("\n{:^10}{:^10}{:^10}{:^10}{:^10}{:^10}{:^10} ".format("i","xi","xs", "xa", "signo", "cambio", "error"))

while(abs( f(xa)) > error and i < itmax):
    i += 1
    xa = (xi + xs)/2.0
    if f(xi) * f(xa) < 0:
        xs = xa
        signo = "negativo"
        limite = "superior"
    else: 
        xi = xa
        signo = "positivo"
        limite = "inferior"

    print ("{:^10}{:^10.4f}{:^10.4f}{:^10.4f}{:^10}{:^10}{:^10.4f}".format(i,float(xi),float(xs),float(xa),signo, limite,float(f(xa))))

print "Raiz: ", xa