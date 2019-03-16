import sys
import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K

K.clear_session

data_entrenamiento='./Data/Entrenamiento'
data_validacion='./Data/Validacion'

#Parametros
epocas=20
altura, longitud= 100,100
batch_size=32
pasos=1000
pasos_validacion=200
filtrosConvul=32
filstrosConvul2=64
tamano_filtro=(3,3)
tamano_filtro2(2,2)
tamano_pool=(2,2)
clases=3
lr=0.0005

#Pre procesamiento de imagenes