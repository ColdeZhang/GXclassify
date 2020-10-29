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
tf.__version__




def get_images(directory):
    Images = []
    label = 0
    Labels = []  
    
    for labels in os.listdir(directory): #Main Directory where each class label is present as folder name.
        if labels == 'battery': #Folder contain Glacier Images get the '2' class label.
            label = 0
        elif labels == 'paper':
            label = 1
        elif labels == 'bottle':
            label = 2
        elif labels == 'orange':
            label = 3
        elif labels == 'can':
            label = 4
     
        
        for image_file in os.listdir(directory+labels): #Extracting the file name of the image from Class Label folder
            
            
            
            image = cv2.imread(directory+labels+r'/'+image_file) #Reading the image (OpenCV)
            
        
            image = cv2.resize(image,(150,150))
       
            
            #Resize the image, Some images are different sizes. (Resizing is very Important)
            Images.append(image)
            Labels.append(label)
    
    return shuffle(Images,Labels,random_state=817328462) #Shuffle the dataset you just prepared.

def get_classlabel(class_code):
    labels = {0:'电池', 1:'废纸', 2:'瓶子', 3:'橘子皮', 4:'易拉罐'}
    
    return labels[class_code]



new_model = tf.keras.models.load_model('my_model4.h5')


def pred_name():
    pred_images,no_labels = get_images('image.jpg')  #目录结构
    pred_images = np.array(pred_images)
    #pred_images.shape
    rnd_number = randint(0,len(pred_images))
    pred_image = np.array(pred_images)
    pred_class = get_classlabel(new_model.predict_classes(pred_image)[0])
    pred_prob = new_model.predict(pred_image).reshape(5)
    print(pred_class)
    print(pred_prob)
    return pred_class