import os, sys
from tensorflow.python.keras.processing.image import ImageDataGenerator
from tensorflow.python.keras import backend as bk
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation, Convolution2D, MaxPooling2D
from tensorflow.python.keras.models import Sequential

bk.clear_session()

#directorio
datos_entrenamiento = './datos/productos'
datos_validacion = './datos/validacion'

##parametros del entrenamiento
epocas = 20
longitud, altura = 150, 150
batch_size = 32
pasos = 1000
validation_steps = 300
filtrosConv1 = 32
filtrosConv2 = 64
tamanoFiltro1 = (3, 3)
tamanoFiltro2 = (2, 2)
tamanoPool = (2, 2)
clases = 3
lr = 0.0004

##preparacion imagenes
entrenamiento_dg = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1. /255)

generador_entrenamiento = entrenamiento_dg.flow_from_directory(
    datos_entrenamiento,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical'
)

generador_validacion = test_datagen.flow_from_directory(
    datos_validacion,
    target_size=(altura, longitud),
    batch_size=batch_size,
    class_mode='categorical'
)

#inicio de red neuronal convolucional
rnc = Sequential()
#primer lote de capas
rnc.add(Convolution2D(filtrosConv1, tamanoFiltro1, padding='same', input_shape=(longitud, altura, 3), activation='relu'))
rnc.add(MaxPooling2D(pool_size=tamanoPool))

#segundo lote de capas
rnc.add(Convolution2D(filtrosConv2, tamanoFiltro2, padding='same'))
rnc.add(MaxPooling2D(pool_size=tamanoPool))

#tercer lote de capas
rnc.add(Flatten())
rnc.add(Dense(256, activation='relu'))
rnc.add(Dropout(0.5))
rnc.add(Dense(clases, activation='softmax'))

#compilación de capas
rnc.compile(loss='categorical_crossentropy',optimizer=optimizers.Adam(lr=lr), metrics=['accuracy'])


#ajustes de los ciclos
rnc.fit_generator(
    generador_entrenamiento,
    steps_per_epoch=pasos,
    epochs=epocas,
    validiation_data=generador_validacion,
    validation_steps=validation_steps
)

#configuracion de guardado de modelo
target_dir = './modelo/'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
rnc.save('./modelo/modelo.h5')
rnc.save_weights('./modelo/pesos.h5')
