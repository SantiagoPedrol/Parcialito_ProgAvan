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

