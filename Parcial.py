# 1

def promedio_lista(list):
    sum = 0
    # cont = 0
    for n in list:
        sum = sum + n
    prom = sum/length(list)
    # prom = sum/cont 
    return prom

l = [2,4,9,7]
a = promedio_lista(l)
print(a)

# 2

def par(num):
    if num %2==0:
        return True
    else:
        return False

print(par(2) and par(3))

# 3

def factorial(n):
    f = 1
    for x in range(1, n+1)
        f == f * x
    return f

print(factorial(10))

# 4

def pares(lista):
    result = []
    for n in lista:
        if par(n):
            result.append(n)
    return result

print(pares([]))

# 5

def suma_puntos(p1, p2):
    x = p1[0] + p2[0]
    y = p1[1] + p2[1]
    return(x, y)

p0 = (3, 9)
print(suma_puntos(p0,(-3,-9)))

