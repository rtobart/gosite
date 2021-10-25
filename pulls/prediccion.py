import numpy as np
from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array

#carga del modelo y peso del modelo
longitudaltura = (150, 150)
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
rnc = load_model(modelo)
rnc.load_weights(pesos_modelo)

#función de predicción
def predecir(archivo):
    #carga y formato imagen a predecir
    x = Image.open(archivo)
    x = x.resize(longitudaltura, Image.ANTIALIAS)
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
    elif respuesta == 2:
        tipo = "pesa rusa"
    return tipo
