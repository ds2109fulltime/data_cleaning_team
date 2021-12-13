import cv2 as cv
import os
import numpy as np

def read_images(path):
    '''
    This function reads an image from a path.
    Parameters:
    - path: Path where the image is.
    '''
    image = cv.imread(path)
    return image

def flip_img(pathsIn, pathsOut):
    
    '''
    This function receives the paths where the images are and flip them (mirror effect).
    Parameters:
    - pathsIn: Paths where the images are. It is an iterable.
    - pathsOut: Paths where the images will be saved. It is an iterable.
    '''

    for i in range(len(pathsIn)):
        filenames = os.listdir(pathsIn[i])
        count = 0
        for file in filenames:
            if file not in os.listdir(pathsOut[i]):
                try: 
                    print('Flipping: ', count+1)
                    path_img = pathsIn[i] + '\\' + file
                    image = read_images(path_img)
                    flip = cv.flip(image, 1)
                    cv.imwrite(pathsOut[i] + '\\' + file, flip)
                    count = count + 1
                except:
                    break
            else:
                pass

        print('***********************')
        print('Images in folder {} fipped.'.format(pathsIn[i]))
        print('***********************')



def resize_img(images, height, width):
    
    '''
    This function receives images and returns them resized with the specified dimensions.
    Parameters:
    - images: array of images. It is an iterable.
    - height: height in ppp
    - width: width in ppp
    '''

    resized_images = []

    for image in images:
        resized = cv.resize(image, (height, width))
        resized_images.append(resized)
    
    return np.array(resized_images)


def color2gray(images):
    
    '''
    Esta función recibe las imágenes en un iterable y las devuelve en escala de grises.
    Parámetros:
    - images: array of images. It is an iterable.
    '''

    grey_images = []

    for image in images:
        grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        grey_images.append(grey)
    
    return np.array(grey_images)


def edit_image(images, alpha = 1, beta = 0):
    
    '''
    This function modifies contrast and bright of an array of images.
    Parámetros:
    - images: array of images. It is an iterable.
    - alpha: (1.0-3.0). Contrast controller. The higher it is, the higher is the contrast.
    - beta: (0-100). Bright controller. The higher it is, the higher is the bright.
    '''
    edited_images = []

    for image in images:

        adjusted = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
            
        edited_images.append(adjusted)
    
    return np.array(edited_images)


def negative_colors(images): 
    
    '''
    This function receives an array of images and returns it with the negative colors.
    Parameters:
    - images: array of images. It is an iterable.
    '''

    negative_images = []

    for image in images:
        negative = 255 - image
        negative_images.append(negative)
    
    return np.array(negative_images)


def monocolor(images, color = 'blue'):
    
    '''
    This function receives an array of images and the color channel (red, green o blue) and returns them into this channel.
    Cambia a azul ('blue') si no se especifica.
    Parameters:
    - images: array of images. It is an iterable.
    - color: color channel we want to get (red, green, blue).
    '''
    monocolor_images = []

    for image in images:

        if color == 'blue':
            b = image.copy()
            b[:,:,0] = b[:,:,1] = 0
            channel = b
        
        elif color == 'green':
            g = image.copy()
            g[:,:,0] = g[:,:,2] = 0
            channel = g
        
        elif color == 'red':
            r = image.copy()
            r[:,:,1] = r[:,:,2] = 0
            channel = r
        
        else:
            print('Error: Chose the correct color.')
            break
        
        monocolor_images.append(channel)

    return np.array(monocolor_images)