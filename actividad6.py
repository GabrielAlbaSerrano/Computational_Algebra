# Autores: Celeste Rhodes Rodríguez y Gabriel Alba Serrano

def f(n,m):
    phi1 = 2**(m+2) * 5**(m-2)
    r1 = n % phi1
    phi0 = 2**(m+1) * 5**(m-1)
    r0 = pow(7,r1,phi0)
    return pow(3,r0,10**m)

""""
    Explicación del programa y como hemos implementado la función f:
    Queremos calcular 3**7**n (mod 10**m)
    
    La idea es reducir la cantidad de cálculo y de operaciones, "queremos
    hacer los números más pequeños para poder operar con ellos más fácilmente".
    Para ello vamos a utilizar el Teorema de Euler-Fermat.
    Sabemos que: 
        10**m = (2**m) * (5**m)
    Luego 3 y 10**m son coprimos porque no comparten ningún factor primo, 
    es decir, gcd(3,10**m)=1
    Por lo tanto:
        3**phi(10**m) = 1 mod(10**m) , siendo phi la función phi de Euler
    
    Tenemos que descomponer 7**n de tal manera que:
        7**n = c0 * phi(10**m) + r0 , 0 <= r0 < phi(10**m)
    Así:
        3**7**n = 3**(c0 * phi(10**m) + r0) = (3**phi(10**m))**c0 * 3**r0 =
                = 3**r0 (mod 10**m)
        
    Observamos que 7**n = r0 (mod phi(10**m))
    Sabemos por definición de phi que:
        phi(10**m) = 10**m * (1-1/2) * (1-1/5) = 10**m * 1/2 * 4/5 =
                   = 10**m * 2/5 = 2**(m+1) * 5**(m-1)
    Como 7 y phi(10**m) son coprimos, podemos aplicar de nuevo el Teorema de 
    Euler-Fermat:
        7**phi(phi(10**m)) = 1 (mod phi(10**m))
    
    Dividimos n entre phi(phi(10**m)):
        n = c1 * phi(phi(10**m)) + r1 , 0 <= r1 < phi(phi(10**m))
    Sustituimos:
        7**n = 7**(c1 * phi(phi(10**m)) + r1) = (7**phi(phi(10**m)))**c1 * 7**r1 =
             = 7**r1 (mod phi(10**m)) = r0 (mod phi(10**m))
        
    Para calcular phi(10**m) y phi(phi(10**m)) hemos definido las variables 
    phi0 y phi1:
        phi0 = phi(10**m) = 2**(m+1) * 5**(m-1)
        phi1 = phi(phi(10**m)) = phi(10**m) * (1-1/2) * (1-1/5) = 
             = 2**(m+1) * 5**(m-1) * 2/5 = 2**(m+2) * 5**(m-2) 
"""
