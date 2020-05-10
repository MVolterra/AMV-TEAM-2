import pandas as pd


# Ejercicio Primos

def primo(x):
    if x == 1:
        return 1
    else:
        y = 2
        while x % y != 0:
            y += 1
        if x == y:
            return 1
        else:
            return 0


def archivo(x):
    if primo(x) == 0:
        arch = open('primos.txt', 'w')
        lst = []
        for i in range(x):
            if primo(i) == 1:
                lst.append(i)
        arch.write(",".join(["%d" % x for x in lst]))
        arch.close()
        return lst
    else:
        for i in range(1, x + 1):
            arch = open('piramide_%d.txt' % i, 'w')
            for k in range(1, i + 1):
                arch.write("*" * k)
                arch.write("\n")
            arch.close()
        return i


print(archivo(3))

##############################################
# Ejercicio Fibonacci

def Fibo(x):
    if x == 1 or x == 2:
        return 1
    else:
        fib = [1, 1]
        c = 1
        while c != x:
            z = fib[c] + fib[c - 1]
            fib.append(z)
            c += 1
        return fib


# def fibo(x, ls=None):
#    if ls is None:
#       ls = [1, 1]
#  t = len(ls)
# if x != t:
#     y = ls[t - 1] + ls[t - 2]
#        ls.append(y)
#       iter(x, ls)
#  else:
#    return ls
print(Fibo(5))
#####################################

# Ejercicio Runge-Kutta

