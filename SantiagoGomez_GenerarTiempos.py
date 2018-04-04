import numpy as np
import time

#Funcion que calcula el N-esimo termino de la serie de fibonacci
def fibonacci(N):
    if(N == 1 or N == 2):
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)

#Funcion que da el tiempo de calcular Fibonacci(N)
def get_time(N):
    t0 = time.time()
    r = fibonacci(N)
    t1 = time.time() - t0
    return t1

N = 35
n = range(1,N+1)
fibo = []
t = []

#Calcula el tiempo de computacion de los primeros cuarenta terminos de fibonacci
for i in n:
    print i, get_time(i)
    
        
