# Autores: Celeste Rhodes Rodrí­guez y Gabriel Alba Serrano

def f(n,m):
    phi1 = 2**(m+2) * 5**(m-2)
    r1 = n % phi1
    phi0 = 2**(m+1) * 5**(m-1)
    r0 = pow(7,r1,phi0)
    return pow(3,r0,10**m)

