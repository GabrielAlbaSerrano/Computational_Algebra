# Autores: Celeste Rhodes Rodrí­guez y Gabriel Alba Serrano

import natural

# En primer lugar vamos a definir una función exp2(n) que calcule 2 elevado a n
# utilizando los algoritmos y programas de multiplicación vistos en clase

def exp2(n): # n entero mayor que 0
    if n==1: # Caso base: 2 elevado a 1 es igual a 2
        return [2]
    else: # Caso recursivo, distinguimos dos casos:
        if n%2==0: # n es par (n = 2*m)
            # 2**n = 2**(2*m) = (2**2)**m = 4**m = (2*2)**m = (2**m)*(2**m)
            # Definimos w = 2**m = 2**(n//2), para ahorrar coste computacional
            # y así evitar hacer la misma recursión dos veces
            w = exp2(n//2)
            return natural.multiplicar_karatsuba(w,w)
        else: # n es impar (n = 2*m + 1)
            # 2**n = 2 * 2**(n-1)
            return natural.multiplicar([2],exp2(n-1))

# Definimos la función que pasa un número binario a decimal, ambos expresados
# como listas de enteros
# Vamos a utilizar una recursión para esta función, utilizando además la
# función exp2(n)

def base2_a_decimal(a):
    n=len(a)
    if n<=1: # Caso base
        return a
    else: # Caso recursivo
        # Basándonos en el algoritmo de Karatsuba, dividimos la lista a en dos
        # partes (a1 y a0)
        a0 = base2_a_decimal(a[:n//2])
        a1 = base2_a_decimal(a[n//2 :])
        # Observamos que a1 en cada caso recursivo tiene que ser multiplicado
        # por 2**(n//2)
        b = natural.multiplicar_karatsuba(exp2(n//2), a1)
        # Devolvemos la función recursiva: a = a1*2**(n//2) + a0
        return natural.sumar(a0,b)

# Con este algoritmo hemos obtenido una complejidad binaria O(n**(log2(3)))

# La siguiente función es análoga a la anterior, excepto porque tiene memoria
# No hay diferencias significativas en el tiempo de ejecución de la función sin
# memoria vs la que tiene memoria, ambas tardan entre 28 y 29 segundos en el test

def base2_a_decimal_con_memoria(a):
    n=len(a)
    mem={}
    if tuple(a) in mem:
        return mem[a]
    if n<=1:
        return a
    else:
        a0 = base2_a_decimal(a[:n//2])
        a1 = base2_a_decimal(a[n//2 :])
        b = natural.multiplicar_karatsuba(exp2(n//2), a1)       
        result = natural.sumar(a0,b)
        mem[tuple(a)] = result
        return result