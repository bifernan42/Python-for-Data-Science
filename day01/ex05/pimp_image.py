from load_image import ft_load
import numpy as np
from pathlib import Path
import cv2
import sys
from load_image import ft_load
import matplotlib.pyplot as plt

def ft_invert(array) -> np.array:
    """
    +, -, *
    """
    return np.array(255 - array[:,:,:])


    #your code here

def ft_red(array) -> np.array:
    """
        *
    """
    #print(len(array[0][0]))

    #print([i = for i in array[:,:]])
    #your code here
    return array * [1,0,0]


def ft_green(array) -> np.array:
    """
        -
    """
    #your code here
    return array - array[:][:][

def ft_blue(array) -> np.array:
    """
        =
    """
    #your code here

def ft_grey(array) -> np.array:
    """
        /
    """
    #your code here

def display_image(image):
    plt.imshow(image)
    plt.show()


image = ft_load("animal.jpeg")
image = ft_red(image)

display_image(image)
