import numpy as np
from pathlib import Path
import cv2
import sys
from load_image import ft_load
import matplotlib.pyplot as plt


def rotate(path: str, width: int, height: int):
    image = ft_load(path)
    print(len(image[0]))
    print(len(image))
    transposed = np.array([[image[j][i] for j in range(0, len(image))] for i in range(0, len(image[0]))])
    print(f"New shape after Transpose: {transposed.shape[:2]}")
    imgplot = plt.imshow(transposed) 
    plt.show()




rotate("animal.jpeg", 0,0)

