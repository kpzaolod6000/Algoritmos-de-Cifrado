import numpy as np
from preprocPlayFair import preproces,replaceCharacters,replaceDecrypt

def KeyMatrix(key,tam_matrix):
    result = []
    letters_my  = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    letters_N   = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    key = replaceCharacters(key,tam_matrix)

    if(tam_matrix == 5):
        for item in key:
            if item not in result:
                result.append(item)
                letters_my = letters_my.replace(item,"")
    
        for item in letters_my:
            result.append(item)
        result  = np.array(result)
        
    else :
        for item in key:
            if item not in result:
                result.append(item)
                letters_N = letters_N.replace(item,"")
    
        for item in letters_N:
            result.append(item)
        result  = np.array(result)
    
    # print(result)
    KeyMatrix_ = result.reshape(tam_matrix,tam_matrix)
    
    return KeyMatrix_


def CipherPF(message,key,tam_matrix):
    message = preproces(message,tam_matrix)
    keyMatrix_ = KeyMatrix(key,tam_matrix)
    
    wordPairs = message.split(" ")
    
    textEncryptd = "";
    for item in wordPairs:
        p = item[0]
        q = item[1]
    
        posP = np.where(keyMatrix_==p)
        posQ = np.where(keyMatrix_==q)        
        P_i = posP[0][0]
        P_j = posP[1][0]

        Q_i = posQ[0][0]
        Q_j = posQ[1][0]
        
        # print(P_i,P_j," ",Q_i,Q_j)
        # print(keyMatrix_[P_i][P_j], keyMatrix_[Q_i][Q_j])

        if P_i == Q_i : # MISMA FILA
            forward_P = P_j+1
            forward_Q = Q_j+1

            if forward_P >= len(keyMatrix_[P_i]): # mod 5 o 6
                forward_P -= len(keyMatrix_[P_i])

            if forward_Q >= len(keyMatrix_[Q_i]):# mod 5 o 6
                forward_Q -= len(keyMatrix_[Q_i])

            p = keyMatrix_[P_i][forward_P]
            q = keyMatrix_[Q_i][forward_Q]
            # print(p,q)

        elif P_j == Q_j:# MISMA comlumna
            downward_P = P_i+1
            downward_Q = Q_i+1

            if downward_P >= len(keyMatrix_[P_i]): # mod 5 o 6
                downward_P -= len(keyMatrix_[P_i])

            if downward_Q >= len(keyMatrix_[Q_i]):# mod 5 o 6
                downward_Q -= len(keyMatrix_[Q_i])
            
            p = keyMatrix_[downward_P][P_j]
            q = keyMatrix_[downward_Q][Q_j]
            # print(p,q)
        else :
            p = keyMatrix_[P_i][Q_j]
            q = keyMatrix_[Q_i][P_j]
            # print(p,q)

        textEncryptd += p + q + " ";

    # print(message)
    # print(keyMatrix_)
    # print(textEncryptd)
    return textEncryptd,keyMatrix_,message




def DecryptPF(message,key,tam_matrix):
    message = replaceDecrypt(message,tam_matrix)
    
    keyMatrix_ = KeyMatrix(key,tam_matrix)
    
    wordPairs = message.split(" ")
    print(wordPairs)
    # print(wordPairs)
    
    textDecrypt = "";
    for item in wordPairs:
        p = item[0]
        q = item[1]
    
        posP = np.where(keyMatrix_==p)
        posQ = np.where(keyMatrix_==q)        
        P_i = posP[0][0]
        P_j = posP[1][0]

        Q_i = posQ[0][0]
        Q_j = posQ[1][0]
        
        # print(P_i,P_j," ",Q_i,Q_j)
        # print(keyMatrix_[P_i][P_j], keyMatrix_[Q_i][Q_j])

        if P_i == Q_i : # MISMA FILA
            forward_P = P_j-1
            forward_Q = Q_j-1

            if forward_P < 0: # mod 5 o 6
                forward_P += len(keyMatrix_[P_i])

            if forward_Q < 0:# mod 5 o 6
                forward_Q += len(keyMatrix_[Q_i])

            p = keyMatrix_[P_i][forward_P]
            q = keyMatrix_[Q_i][forward_Q]
            # print(p,q)

        elif P_j == Q_j:# MISMA comlumna
            downward_P = P_i-1
            downward_Q = Q_i-1

            if downward_P < 0: # mod 5 o 6
                downward_P += len(keyMatrix_[P_i])

            if downward_Q < 0:# mod 5 o 6
                downward_Q += len(keyMatrix_[Q_i])
            
            p = keyMatrix_[downward_P][P_j]
            q = keyMatrix_[downward_Q][Q_j]
            # print(p,q)
        else :
            p = keyMatrix_[P_i][Q_j]
            q = keyMatrix_[Q_i][P_j]
            # print(p,q)

        textDecrypt += p + q + " ";

    return textDecrypt,keyMatrix_,message


# message = input("Introducir Mensaje: ")
# key     = input("Key: ")
# CipherPF(message,key)