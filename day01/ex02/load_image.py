import numpy as np
from pathlib import Path

def ft_load(path: str) -> array:
    """
        This function loads an image, prints its format, and its pixels
        content in RGB format.
    """
    p = Path(path)
    assert p.is_file(), f"File {path} does not exist"


    with p.open() as image: #traitment image

