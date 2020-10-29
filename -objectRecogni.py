import tensorflow.keras.layers as Layers
import tensorflow.keras.activations as Actications
import tensorflow.keras.models as Models
import tensorflow.keras.optimizers as Optimizer
import tensorflow.keras.metrics as Metrics
import tensorflow.keras.utils as Utils
from keras.utils.vis_utils import model_to_dot
import os
import matplotlib.pyplot as plot
import cv2
import numpy as np
from sklearn.utils import shuffle
from sklearn.metrics import confusion_matrix as CM
from random import randint
from IPython.display import SVG
import matplotlib.gridspec as gridspec
import tensorflow as tf
import keras



new_model = tf.keras.models.load_model('res/or_model/my_model5.h5')
new_model.summary()


def get_images(directory):
    Images = []
    label = 0
    Labels = []  
    
    for labels in os.listdir(directory): #Main Directory where each class label is present as folder name.
        if labels == 'cardborad': #Folder contain Glacier Images get the '2' class label.
            label = 2
        elif labels == 'metal':
            label = 4
        elif labels == 'plastic':
            label = 0
        elif labels == 'paper':
            label = 1
        elif labels == 'glass':
            label = 5
        elif labels == 'trash':
            label = 3
        
        for image_file in os.listdir(directory+labels): #Extracting the file name of the image from Class Label folder
            
            
            
            image = cv2.imread(directory+labels+r'/'+image_file) #Reading the image (OpenCV)
            
        
            image = cv2.resize(image,(150,150))
       
            
            #Resize the image, Some images are different sizes. (Resizing is very Important)
            Images.append(image)
            Labels.append(label)
    
    return shuffle(Images,Labels,random_state=817328462) #Shuffle the dataset you just prepared.

def get_classlabel(class_code):
    labels = {2:'cardboard', 4:'metal', 0:'plastic', 1:'paper', 5:'glass', 3:'trash'}
    
    return labels[class_code]
    
def ans():
    pred_images,no_labels = get_images('res/or_input_res/seg_pred/')
    pred_images = np.array(pred_images)
    print(pred_images.shape)
    pred_class = get_classlabel(new_model.predict_classes(pred_images)[0])
    print(pred_class)
    return pred_class

