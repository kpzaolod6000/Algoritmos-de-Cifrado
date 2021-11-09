def main():
    message = input("Introducir Mensaje: ")
    key     = int(input("Key [1-26]: "))
    mode    = input("Cifrar o Descifrar [c/d]: ")

    if mode.lower().startswith('c'):
        mode = "cifrar"
    elif mode.lower().startswith('d'):
        mode = "descifrar"

    translated = encdec(message, key, mode)
    if mode ==   "cifrar":
        print(("Mensaje Cifrado:", translated))
    elif mode == "descifrar":
        print(("Mensaje Descifrado:", translated))
        
def encdec(message, key, mode):
    translated   = ""
    letters_my   = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    letters_mn   = "abcdefghijklmnñopqrstuvwxyz" 
    for symbol in message:
        if symbol in letters_my:
            num = letters_my.find(symbol)
            if mode ==   "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(letters_my):
                num -= len(letters_my)
            elif num < 0:
                num += len(letters_my)

            translated += letters_my[num]

        elif symbol in letters_mn:
            num = letters_mn.find(symbol)
            if mode ==   "cifrar":
                num = num + key
            elif mode == "descifrar":
                num = num - key

            if num >= len(letters_mn):
                num -= len(letters_mn)
            elif num < 0:
                num += len(letters_mn)

            translated += letters_mn[num]
        else:
            translated += symbol
    return translated