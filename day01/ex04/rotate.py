import numpy as np
from pathlib import Path
import cv2
import sys

def zoom_image(path: str, width: int, height: int):
    image = ft_load(path)
   



    transposed = [image[j][i] for j in range()]
    
    print(f"New shape after Transpose: {transposed.shape[:2]}")
    imgplot = plt.imshow(zoomed_in) 
    plt.show()
