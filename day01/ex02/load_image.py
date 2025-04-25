import numpy as np
from pathlib import Path

def try_and_except(condition: bool, message: str):
    """
        This function tries condition, prints message and exits if an error is raised
    """
    try:
        assert condition, f"{message}"
    except AsertionError as e:
        print(f"AssertionError: {e}")
        exit()

def scan_image(image: file) -> None:
    """
        This function retrieves information
        about the image and prints them
    """



def ft_load(path: str) -> np.ndarray:
    """
        This function loads an image, prints its format, and its pixels
        content in RGB format.
    """
    p = Path(path)
    try_and_except(p.is_file()), f"File {path} does not exist")
    try:
        with p.open() as image:
            #traitement image



    except Exception as e:
        print("{e}: couldn't open file !")
