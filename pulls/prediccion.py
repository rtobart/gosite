import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array

#carga del modelo y peso del modelo
longitud, altura = 150, 150
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
rnc = load_model(modelo)
rnc.load_weights(pesos_modelo)

#función de predicción
def predecir(archivo):
    #carga y formato imagen a predecir
    x = load_img(archivo, target_size=(longitud,altura))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    #llamada al modelo
    arreglo = rnc.predict(x)
    resultado = arreglo[0]
    respuesta = np.argmax(resultado)
    tipo = ""
    if respuesta == 0:
        tipo = "barra olimpica"
    elif respuesta == 1:
        tipo = "mancuerna"
    elif respuesta == 3:
        tipo = "pesa rusa"
    return tipo
    
