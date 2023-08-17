# Autores: Celeste Rhodes Rodrí­guez y Gabriel Alba Serrano

import math
import random

def p(m): # m número natural
    result = 1
    for i in range(m):
        result *= (3*i+1)
    return result

def test_pm_plus_1(m):
    N = p(m)+1
    testRB = es_primo_rabin_miller(N,25)
    if testRB == 'Probablemente primo':
        # es_primo_lucas puede devolver 'Probablemente compuesto'
        # y habría una contradicción con testRB, pero esta situación es
        # altamente improbable que ocurra debido al elevado número de intentos
        return es_primo_lucas(N,25) 
    else:
        return testRB
    
def es_primo_rabin_miller(N,intentos):
    if N in {2, 3, 5, 7}:
        return True
    if N < 11:
        return False
    if N % 2 == 0:
        return False
    r = 0
    m = N-1
    while m % 2 == 0:
        m //= 2
        r += 1
    for i in range(intentos):
        a = random.randint (1, N-1)
        if math.gcd (a,N) != 1:
            return False
        x = pow(a, m, N)
        esta_en_T_N = (x == 1) or (x == N-1)
        t = 0
        while not esta_en_T_N and t < r-1:
            x = pow(x, 2, N)
            esta_en_T_N = (x == N-1)
            t += 1
        if not esta_en_T_N :
            return False
    return 'Probablemente primo'

def es_primo_lucas(N,intentos):
    for k in range(intentos):
        testlucas = lucas(N)
        if testlucas != 'Indeterminado':
            return testlucas
    return 'Probablemente compuesto'

def lucas(N):
    #Elegimos a aleatorio en el intervalo [2,N]  
    a = random.randint (2,N-1)
    #Aplicamos el Teorema de Euler-Fermat
    if pow(a,N-1,N) != 1:
        return False
    else:
    #Sabemos que N-1 = q1**s1 * q2**s2 * ... * qr**sr , tal que q1,...,qr son primos
    #Para reducir el número de operaciones vamos a expresar N-1 = u*v, siendo:
    # u = q1**(s1 -1) * ... * qr**(sr -1)
    # v = q1 * q2 * ... * qr
    #Definimos: x = pow(a,u,N)
    #Además para cada primo q que divide a N-1 calculamos: y = pow(a,v//q,N)
    #Finalmente comprobamos si para cada q:
    # pow(a,(N-1)//q,N) = (x*y)%N != 1
    #Entonces N es primo por el Teorema de Lucas
    #Observación: El coste computacional de calcular para cada q
    # pow(a,(N-1)//q,N) es mucho mayor que calcular x*y (mod N),
    #ya que x hay que calcularlo una únicamente vez, e, y requiere menos operaciones
        v = 1
        l = divprimos_pm(N-1) # N-1 = p(m)
        for q in l:
            v *= q
        u = (N-1)//v
        x = pow(a,u,N)
        for q in l:
            y = pow(a,v//q,N)
            if (x*y)%N == 1:
                return 'Indeterminado'
        return True

#La siguiente función devuelve una lista de divisores primos de un entero p(m)
#La idea de esta función es comprobar si un número d es primo y divide a n,
#en ese caso dividimos n por d hasta que no se pueda dividir más
def divprimos_pm(n):
    result = []
    if n%2 == 0:
        result += [2]
        n = aux(n,2)
    #Como p(m) = 1 (mod 3) para todo m número natural, entonces 3 no es divisor
    #de p(m), por ello empezamos por d = 5
    #Observación:
    # 1,2,3,4
    # 5,6,7,8,9,10
    # 11,12,13,14,15,16
    # 17,18,19,20,21,22
    # 23,24,25,26,27,28
    # 29,30,31,32,33,34
    #Nos fijamos que cada 6 números desde el 5, sólamente dos de ellos no son
    #múltiplos de 2 ó de 3, y por lo tanto candidatos a ser divisores primos
    d = 5
    while d < (n//d +1):
        if n%d == 0:
            if es_primo(d):
                result += [d]
                n = aux(n,d)
        if n%(d+2) == 0:
            if es_primo(d+2):
                result += [d+2]
                n = aux(n,d+2)
        d += 6
    if es_primo(n):
        return result + [n]
    else:
        return result
    
def aux(n,d):
    while n%d==0:
        n = n//d
    return n

def es_primo(x):
    if x < 2:
        return False
    else:
        raiz = raiz_cuadrada_super_rapida(x)
        y = 2
        while y <= raiz:
            if x % y == 0:
                return False
            y += 1
    return True

def raiz_cuadrada_super_rapida(x):
    izq = 0
    der = x+1
    while izq < der-1:
        med = (izq+der)//2
        if med*med <= x:
            izq = med
        else:
            der = med
    return izq

#Hemos comprobado varios casos y la función calc no reduce considerablemente
#el coste computacional, por ello no la hemos utilizado en nuestro programa
def calc(a,l,N):
    n = len(l)
    if n==1:
        return [a]
    if n==2:
        return [pow(a,l[0],N),pow(a,l[1],N)]
    else:
        l1 = l[:n//2]
        l2 = l[n//2:]
        P1 = 1
        P2 = 1
        for i in range(len(l1)):
            P1 *= l1[i]
        for i in range(len(l2)):
            P2 *= l2[i]
        result = []
        c1 = calc(a,l1,N)
        c2 = calc(a,l2,N)
        for i in range(len(c1)):
            result += [pow(c1[i],P2,N)]
        for i in range(len(c2)):
            result += [pow(c2[i],P1,N)]
        return result

