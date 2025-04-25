import numpy as np
from pathlib import Path
from load_image import load_image

def zoom_image(path: str, x: int, y: int):
    image = load_image(path)[x:, y:]
    print("New shape after slicing: {shape} or {shape[:2]}")

