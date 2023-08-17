"""
De: Gabriel Alba Serrano y Celeste Rhodes Rodriguez
"""

def es_suma_de_k_potencias_n (x,k,n): 
    l=[]
    #Creamos una lista vacia donde vamos a añadir la terna [x,k,n] que cumpla que x se puede expresar como suma de k numeros enteros positivos
    #elevados a la n-esima potencia (realmente no es necesario añadir la constante n)
    #Todo esto lo hacemos para ahorrar coste computacional, y evitar repetir operaciones y recursiones.
    
    if int(x**(1/n))**n==x or (int(x**(1/n))+1)**n==x: #para evitar los errores de aproximacion del ordenador, por ejemplo 64**(1/3).
          i=round(x**(1/n))
    else:
          i=int(x**(1/n))

    
    #Casos bases de la recursion:
    if x==0 or [x,k,n] in l:
      return True
    elif x<=k: #Caso en el cual x se puede expresar como una suma de k 1's elevados a n
        l.append([x,k,n])
        return True
    elif k==0:
      return False
    elif x==1:
      return True
    
    
    #Caso recursivo
    else:
        #Creamos un bucle en el que vamos recorriendo los numeros enteros que pertenecen al intervalo [0,int(x**(1/n))], comprobando si
        #se que cumple lo que pide el enunciado del ejercicio
        for j in range(0, i+1):
            if es_suma_de_k_potencias_n_aux(x-j**n,k-1,n,j,l): #hacemos la recursion en una funcion auxiliar porque queremos llevar la cuenta de "comienzo".
              l.append([x,k,n])
              return True
        #Si terminamos el bucle sin que devuelva True, x no se puede expresar como suma de k enteros positivos elevados a n
        return False

#A continuacion está la funcion auxiliar que usamos a la hora de hacer la recursion

def es_suma_de_k_potencias_n_aux(x,k,n,comienzo,l):
    if int(x**(1/n))**n==x or (int(x**(1/n))+1)**n==x:
      i=round(x**(1/n))
    else:
      i=int(x**(1/n))
    
    if x==0 or [x,k,n] in l:
      return True
    elif x<=k: 
      l.append([x,k,n])
      return True
    elif k==0:
      return False
    elif x==1:
      return True

    else:
      
      for j in range(comienzo, i+1):
        if es_suma_de_k_potencias_n_aux(x-j**n,k-1,n, j,l):
            comienzo = j #avanzamos si lo hemos encontrado
            l.append([x,k,n])
            return True
      return False
  