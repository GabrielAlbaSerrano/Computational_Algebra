def eliminar5(n):
    #Convertimos el entero n en una cadena de caracteres
    s=str(n) 
    r="" 
    #En r vamos a ir añadiendo los caracteres de s que son diferentes a 5
    for i in range(len(s)):
        if s[i]!='5':
            r=r+s[i]
    #Es importante observar que el comando int no funciona con la cadena vacía "" y con "-"
    if r=="" or r=="-": 
        result=0
    else:
        result=int(r)
    return result
