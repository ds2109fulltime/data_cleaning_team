import pandas as pd
import numpy as np

def images_dataset_properties(images):
    
    '''
    This function receives an array of images and returns its .ndim, .shape y .size
    Parameters:
     - images: array with the images. It is an iterable.
    '''

    print("Dimensiones:",images.ndim)
    print("Shape:",images.shape)
    print("Size:",images.size)