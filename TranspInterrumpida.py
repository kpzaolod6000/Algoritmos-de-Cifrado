def getKey(clave):
    keyArray = list(clave)
    keyInt = list(range(1,len(keyArray)+1))
    convertedKey = [0 for col in range(len(keyArray))]
    keyArray.sort()
    for i in range(len(keyArray)):
        for j in range(len(clave)):
            if(keyArray[i] == clave[j] and convertedKey[j] == 0):
                convertedKey[j] = keyInt[i]
                break
    return convertedKey

def elimtilde(linea):
    nlinea = linea
    nlinea = nlinea.replace('á','a')
    nlinea = nlinea.replace('é','e')
    nlinea = nlinea.replace('í','i')
    nlinea = nlinea.replace('ó','o')
    nlinea = nlinea.replace('ú','u')
    return nlinea

def desencriptar(texto,clave):
    result = ""
    
    #LIMPIAR TEXTO
    texto_limp = texto.upper()
    texto_limp = texto_limp.replace(' ','')
    texto_limp = elimtilde(texto_limp)
    
    #Aux
    iterador = 0
    caracteres = 0
    modifier = 0
    keyArray = getKey(clave.upper())
    matriz = []
    while(caracteres < len(texto_limp)):
        matriz.append(["0" for col in range(len(keyArray))])
        tofind = (iterador%len(keyArray))+1
        for i in range(len(keyArray)):
            if(tofind == keyArray[i]):
                modifier = i+1
                break
        
        limit = caracteres +modifier
        if(limit >= len(texto_limp)):
            limit = limit - (limit % len(texto_limp))
            
        
        j = 0
        
        for i in range (caracteres,limit):
            matriz[iterador][j] = "-"
            j=j+1
        
        iterador = iterador+1
        
        caracteres = caracteres+modifier
    
    #HALLAMOS
    charpos = 0
    for j in range(len(keyArray)):
        k=0
        for i in range(len(keyArray)):
            if(j+1 == keyArray[i]):
                k=i
                break
        
        for i in range(len(matriz)):
            c = matriz[i][k]
            if (c == '-'):
                matriz[i][k] = texto_limp[charpos]
                charpos = charpos +1
        
    for i in range(len(matriz)):
        for l in range(len(keyArray)):
            if(matriz[i][l] != "0"):
                result = result +matriz[i][l]
                
        

    
    # print(result)
    
    return result
    
# desencriptar("HEESPNI RR SSEES EIY A SCBT EMGEPN ANDI CT RTAHSO IEERO","CONVENIENCE")

# print(len("EESPNIRRSSEESEIYASCBTEMGEPNANDICTRTAHSOIEERO"))