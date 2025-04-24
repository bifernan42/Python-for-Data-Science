def check_types(lst: list) -> bool:
    """
        This function checks the type
    """
    if not isinstance(lst, list):
        return False
    for item in lst:
        if not isinstance(item, int | float):
            return False
    return True

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
        This function takes 2 lists of integers or floats in input
        and returns a list of BMI values.
    """
    try:
        assert check_types(height) and check_types(weight), \
                "bad type!"
        assert len(height) == len(weight), \
                "lists size do not match"
    except AssertionError as e:
            print(f"AssertionError: {e}")
            exit()
    return ([k := w / h**2 for (h, w) in zip(height, weight)])

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        This function accepts a list of numbers and an integer representing
        a limit as parameters.
        It returns a list of booleans (True if above the limit).
    """
    try:
        assert isinstance(bmi, list) and isinstance(limit, int), \
                "bad type"
    except AssertionError as e:
        print(f"AssertionError: {e}")
    return [value > limit for value in bmi]


h8 = [1.8, 1.5]
w8 = [90, 75]
print(give_bmi(h8, w8))
print(apply_limit(give_bmi(h8, w8), 26))

"""
def foo():
    try:
        #
    except Exception as e:
        assert False, "message"
"""
