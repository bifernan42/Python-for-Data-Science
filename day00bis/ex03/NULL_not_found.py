"""
    Usual way to test for a NaN :
        return num != num

    Usual way to test for None :
        is not None
"""


def NULL_not_found(object: any) -> int:

    if isinstance(object, type(None)) and object is None:
        print(f"Nothing : {object} {type(object)}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese : {object} {type(object)}")
    elif isinstance(object, int) and object == 0 and object is not False:
        print(f"Zero : {object} {type(object)}")
    elif isinstance(object, str) and object == "":
        print(f"Empty : {object} {type(object)}")
    elif isinstance(object, type(False)) and object is not True:
        print(f"Fake : {object} {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0
