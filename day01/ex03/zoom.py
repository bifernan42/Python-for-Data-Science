import numpy as np
from pathlib import Path
from load_image import ft_load
import matplotlib.pyplot as plt
import cv2


def zoom_image(path: str, width: int, height: int):
    image = ft_load(path)
    center_coordinates = np.array(image.shape[:2], dtype = int) / 2
   

    start_w = int(center_coordinates[0] - (width / 2))
    end_w = int(center_coordinates[0] + (width / 2))

    start_h = int(center_coordinates[1] - (height / 2))
    end_h = int(center_coordinates[1] + (height / 2))

    #print(image.shape)
    #print("Type of image :", type(image))
    #print("Type of image insides :", image.dtype)
    #print(center_coordinates)
    #sub = (start_w, end_w, start_h, end_h)
    #print("SUBSHAPE = ", sub)

    zoomed_in = image[start_w:end_w, start_h:end_h]
    
    print(f"New shape after slicing: {zoomed_in.shape} or {zoomed_in.shape[:2]}")
    imgplot = plt.imshow(zoomed_in) 
    plt.show()

zoom_image("animal.jpeg", 400, 400)
