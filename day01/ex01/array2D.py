def check_types(lst: list, types: any) -> bool:
    """
        This function checks the type
    """
    if not isinstance(lst, list):
        return False
    for item in lst:
        if not isinstance(item, types):
            return False
    return True

def try_and_except(condition: bool, message: str):
    """
        This function tries condition, prints message and exits if an error is raised
    """
    try:
        assert condition, f"{message}"
    except AsertionError as e:
        print(f"AssertionError: {e}")
        exit()

def slice_me(family: list, start: int, end: int) -> list:
    """
        This function takes as parameters a 2D array, prints its shape, and returns a
truncated version of the array based on the provided start and end arguments.
    """
    try_and_except(check_types(family, list), "bad type: expected nested lists")
    return family[start:end]


family = [[1.80, 78.4],
[2.15, 102.7],
[2.10, 98.5],
[1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
