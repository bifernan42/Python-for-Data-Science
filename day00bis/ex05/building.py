import sys as sys


def print_info(input: str):
    """
        Gets input string info and prints results
    """
    char_count: int = len(input)
    upper_count: int = 0
    lower_count: int = 0
    punctuation_count: int = 0
    spaces_count: int = 0
    digits_count: int = 0

    for i in range(0, char_count):
        if input[i].islower():
            lower_count += 1
        elif input[i].isupper():
            upper_count += 1
        elif input[i].isspace():
            spaces_count += 1
        elif input[i].isdigit():
            digits_count += 1
        else:
            punctuation_count += 1

    print(f"The text contains {char_count} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{spaces_count} spaces")
    print(f"{digits_count} digits")


def main(argc: int, argv: list) -> int:
    """
        This is the main function of my program.
    """
    sys.tracebacklimit = 0
    assert argc < 3, "Invalid number of arguments, 1 expected."
    try:
        if argc == 1:
            print("What is the text to count?")
            text = input() + "\n"
        else:
            text = argv[1]
        print_info(text)
    except Exception as e:
        print("Something went wrong.", e)


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
