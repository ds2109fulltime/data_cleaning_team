import cv2 as cv
import os
import numpy as np

def load_data(pathIn):
    '''
    Esta función carga las imágenes de una lista de ubicaciones concretas y los asigna a las variables 'images' y 'labels', de modo que retorna
    los 'train' y los 'test' de cada una de ellas en variables distintas. El return serían (X_train, y_train), (X_test, y_test).
    Para el funcionamiento de esto, las carpetas deben estar organizadas del siguiente modo:
    
    para el train: '../ubicacion/train_images/' y dentro estarán las imágenes de cada clase divididas en carpetas, por ejemplo: buildings, forest, mountain, beach

    para el test: '../ubicacion/test_images/' y dentro estarán las imágenes de cada clase divididas en carpetas, por ejemplo: buildings, forest, mountain, beach

    Variables:
    pathIn: Lista con todas las ubicaciones. Es un iterable
    '''
    class_names = os.listdir(pathIn[0])
    class_names_label = {class_name:i for i, class_name in enumerate(class_names)}

    output = []
    
    # Iterate through training and test sets
    for dataset in pathIn:
        
        images = []
        labels = []
        
        print("Loading {}".format(dataset))
        
        # Iterate through each folder corresponding to a category
        for folder in os.listdir(dataset):
            label = class_names_label[folder]
            
            # Iterate through each image in our folder.
            for file in os.listdir(os.path.join(dataset, folder)):
                
                # Get the path name of the image
                img_path = os.path.join(os.path.join(dataset, folder), file)
                
                # Open and resize the img
                image = cv.imread(img_path)
                image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                image = cv.resize(image, (int(image.shape[1]*0.6), int(image.shape[0]*0.6))) 
                
                # Append the image and its corresponding label to the output
                images.append(image)
                labels.append(label)
                
        images = np.array(images, dtype = 'float32')
        labels = np.array(labels, dtype = 'int32')   
        
        output.append((images, labels))

    return output