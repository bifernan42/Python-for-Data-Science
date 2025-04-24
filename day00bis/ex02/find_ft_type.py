def all_thing_is_obj(object: any) -> int:

    if isinstance(object, set):
        print("Set : " + str(type(object)))
    elif isinstance(object, str):
        print(object + " is in the kitchen : " + str(type(object)))
    elif isinstance(object, list):
        print("List : " + str(type(object)))
    elif isinstance(object, dict):
        print("Dict : " + str(type(object)))
    elif isinstance(object, tuple):
        print("Tuple : " + str(type(object)))
    else:
        print("Type not found")
    return 42
