from flask import Flask, jsonify, render_template, request
from Cesar_Cipher_src import encdec
from PlayFair import CipherPF,DecryptPF
from TranspInterrumpida import desencriptar
import numpy as np

app = Flask(__name__) #este se debe especificar en el Procfile asi : web: gunicorn index:app

# app variable para crear rutas del servidor y crear urls

@app.route('/') # ruta de pagina inicial
def home():
    return render_template('home.html')

#Cesar
@app.route('/Cifrado de Cesar') 
def CesarCipher():
    return render_template('CesarCipher.html')

@app.route('/request_Ci_Cesar' , methods=['POST']) 
def requestCiCesar():
    message= request.form['message_']
    key = int(request.form['key_'])
    mode = request.form['c_d']
    result = encdec(message,key,mode)
    # print(result)
    return jsonify({'result' : result})

#Playfair
@app.route('/Cifrado de Playfair') 
def PlayfairCipher():
    return render_template('PlayfairCipher.html')


@app.route('/request_Playfair' , methods=['POST'])
def requestPlayfair():
    message= request.form['messagePF']
    key = request.form['keyPF']
    c_d = request.form['c_d_']
    tam_matrix = int(request.form['tam_matrix']) #int
    # print(tam_matrix*10)

    if(c_d == "Encriptar"):
        result,keyMatrx,preprocess = CipherPF(message,key,tam_matrix)

    elif (c_d == "Desencriptar"):
        result,keyMatrx,preprocess =  DecryptPF(message,key,tam_matrix)
        # preprocess = ""

    keyMatrx = keyMatrx.ravel()
    keyMatrx = ' '.join (keyMatrx)
    return jsonify({'keyMatrx' : keyMatrx , 'result' : result , 'preprocess' : preprocess})

#Transposicion Interrumpida
@app.route('/Transposicion interrumpida') 
def TranspInterrm():
    return render_template('TranspInterrm.html')


@app.route('/request_TransInterrumpida' , methods=['POST'])
def requestTransInterrumpida():
    message= request.form['messageTI']
    key = request.form['keyTI']
    result = desencriptar(message,key) 
    return jsonify({'result' : result})


# este es el archivo que arrancara la aplicacion
if __name__ == "__main__":
    app.run(debug=True);

#app.run(debug=True); esta opcion hace que la aplicacion esta en modo de prueba
#lo que siginifica si hay cambios actualizara automaticamente
#app.run(); aca no esta en modo de prueba