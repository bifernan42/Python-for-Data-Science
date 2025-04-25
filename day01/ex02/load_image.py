import numpy as np
from pathlib import Path
import cv2

def try_and_except(condition: bool, message: str):
    """
        This function tries condition, prints message and exits if an error is raised
    """
    try:
        assert condition, f"{message}"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit()

def scan_image(path):
    """
        This function retrieves information
        about the image and prints them
    """
    image_bgr = cv2.imread(path)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    print(image_rgb.shape)
    print(image_rgb)
    return image_rgb

def ft_load(path: str) -> np.ndarray:
    """
        This function loads an image, prints its format, and its pixels
        content in RGB format.
    """
    p = Path(path)
    try_and_except(p.is_file() and \
            p.suffix in {".jpeg", ".png", ".jpg"}, \
            f"File {path} does not exist")
    try:
        with p.open() as image:
            image = scan_image(p)
    except Exception as e:
        print(f"{e}: couldn't open file !")
    return image
