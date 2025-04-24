import sys as sys


def print_oddness(number: int):
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def handler(number: str):
    assert number.isnumeric() \
            or (number[0] == "-"
                and number[1:].isnumeric()), \
            "argument is not an integer"
    print_oddness(int(number))


def main(argc: int, argv: list) -> int:
    sys.tracebacklimit = 0
    assert argc < 3, \
        "more than one argument are provided"
    if argc == 2:
        handler(argv[1])
    else
        print("\n")
    return 0


main(len(sys.argv), sys.argv)
