def replaceDecrypt(text,tam_matrix):
    text = text.upper()
    if tam_matrix == 5:
        text = text.translate ({ord(c): "" for c in " áéíóúÁÉÍÓÚÑñ!@#$%^&*()[]{};:,./<>¿?\|`~-=_+'0123456789"})
        text = text.replace("J", "I")
    else:
        text = text.translate ({ord(c): "" for c in " áéíóúÁÉÍÓÚÑñ!@#$%^&*()[]{};:,./<>¿?\|`~-=_+'"})
    text = text.replace("\n", "")
    text = text.replace('"', "")
    

    result = ""
    two = 2
    for j in range(len(text)):
        if j >=2:
            if j == two :
                result += " "
                two +=2        
        result += text[j]
    print(result)

    return result

def replaceCharacters(text,tam_matrix):
    text = text.upper()
    if tam_matrix == 5:
        text = text.translate ({ord(c): "" for c in " áéíóúÁÉÍÓÚÑñ!@#$%^&*()[]{};:,./<>¿?\|`~-=_+'0123456789"})
        text = text.replace("J", "I")
    else:
        text = text.translate ({ord(c): "" for c in " áéíóúÁÉÍÓÚÑñ!@#$%^&*()[]{};:,./<>¿?\|`~-=_+'"})
    text = text.replace("\n", "")
    text = text.replace('"', "")
    
    return text


def preproces(message,tam_matrix):
    message = replaceCharacters(message,tam_matrix) 
    
    removeRepet = ""
    i = 0
    while i<(len(message)-1) :
        if message[i] == message[i+1] :
            removeRepet += message[i] + "X"
        else:
            removeRepet += message[i]
        i += 1;
    removeRepet += message[len(message)-1]
    
    if len(removeRepet) % 2 != 0 :
        removeRepet += "X"
    
    result = ""
    two = 2
    for j in range(len(removeRepet)):
        if j >=2:
            if j == two :
                result += " "
                two +=2        
        result += removeRepet[j]

    return result


def main():
    message = input("Introducir Mensaje: ")
    key     = input("Key: ")
    preproces(message)

# main()