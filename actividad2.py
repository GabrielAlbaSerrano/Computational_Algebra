def conway(l,m,n,k):
    #Definimos la matriz result como una matriz de ceros
    result=[[0 for a in range(n)] for b in range(m)]
    #En cada generación gen modificamos la matriz result hasta llegar a la generación k-ésima
    for gen in range(k):
        #En cada generación la matriz l es la matriz result de la generación anterior 
        if gen!=0: 
             l=result
        #Definimos la matriz v que nos va a indicar el número de vecinos que tiene cada celda de la matriz l 
        #en cada generación
        v = [[0 for i in range(n)]for j in range(m)]
        for row in range(m):
             for col in range(n):
                 #Para cada celda de la matriz l veamos cuantos vecinos tiene:
                 #si una celda vecina es igual a 1 entonces sumamos un vecino a v[row][col]
                 #Observamos que los índices row y col tienen que pertenecer a los intervalos [0,m] y [0,n] 
                 #respectivamente, en caso contrario tendremos un error
                 if row-1 in range(m) and col-1 in range(n):
                     if l[row-1][col-1]==1:
                         v[row][col]+=1
                 if row-1 in range(m) and col+1 in range(n):
                     if l[row-1][col+1]==1:
                         v[row][col]+=1
                 if row+1 in range(m) and col-1 in range(n):
                     if l[row+1][col-1]==1:
                         v[row][col]+=1
                 if row+1 in range(m) and col+1 in range(n):
                     if l[row+1][col+1]==1:
                         v[row][col]+=1
                 if row-1 in range(m):
                     if l[row-1][col]==1:
                         v[row][col]+=1
                 if row+1 in range(m):
                     if l[row+1][col]==1:
                         v[row][col]+=1
                 if col-1 in range(n):
                     if l[row][col-1]==1:
                         v[row][col]+=1
                 if col+1 in range(n):
                     if l[row][col+1]==1:
                         v[row][col]+=1
        
        #Una vez que tenemos el número de vecinos de cada celda de l, modificamos la matriz result según las normas
        #de "El juego de la vida" de Conway           
        for row in range(m):
             for col in range(n):
                 if l[row][col]==0:
                     if v[row][col]==3:
                         result[row][col]=1
                     else:
                         result[row][col]=0
                 else:
                     if v[row][col]==2 or v[row][col]==3:
                         result[row][col]=1
                     else:
                         result[row][col]=0
   
    return result
