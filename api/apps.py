from django.apps import AppConfig
import os 
from tensorflow import keras
from tensorflow.keras import backend as K
from django.apps import AppConfig
from django.conf import settings

def contrastive_loss(y_true, y_pred):
    margin = 1
    # print("y_pred",y_pred)
    sqaure_pred = K.square(y_pred)
    margin_square = K.square(K.maximum(margin - y_pred, 0))
    return K.mean(y_true * sqaure_pred + (1 - y_true)* margin_square)


class ApiConfig(AppConfig):
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS,'hwsv_model.h5')
    model = keras.models.load_model(MODEL_FILE,custom_objects = {'contrastive_loss':contrastive_loss})

