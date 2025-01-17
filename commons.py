# IMPORTS
import os
import io

import torchvision.transforms as transforms
import torchvision as tv
import torch
from PIL import Image
import onnx

# CHARGEMENT DU MODELE IA
def get_model():
    # Prétraitement : charger le modèle ONNX
    model_path = os.path.join('models', 'MedNet.onnx')
    model = onnx.load(model_path)
    # Vérifiez le modèle
    try:
        onnx.checker.check_model(model)
    except onnx.checker.ValidationError as e:
        print('The model is invalid: %s' % e)
    else:
        print('The model is valid!')
    return model


def transform_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    img_y = scaleImage(img)
    img_y.unsqueeze_(0)
    return img_y


def format_class_name(class_name):
    class_name = class_name.title()
    return class_name


# Donne une image PIL, retourne un tensor
def scaleImage(x):
    toTensor = tv.transforms.ToTensor()
    y = toTensor(x)
    if (y.min() < y.max()):
        y = (y - y.min()) / (y.max() - y.min())
    z = y - y.mean()
    return z
