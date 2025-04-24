import sys as sys

def main(argc, argv):
    """
        The main function of my program...
        Prints the morse version of your text...
    """
    sys.tracebacklimit = 0

    assert argc == 2, f"wrong number of arguments: expected 1, got {argc - 1}"

    NESTED_MORSE = { " ": "/", "A": ".-", "B": "-...", "C": "-.-.",
    "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--",
    "N": "-.", "O": "---", "P": ".--.", "Q": "--.- ", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",
    "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", 
    "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----."}
    
    result = ""
    input = argv[1]

    for i in range(len(input)):
        assert input[i].isalnum() or input[i].isspace(), \
            f"bad arguments: '{input[i]}'"
        result += NESTED_MORSE[input[i].upper()]
        if i < len(input) - 1:
            result += " "

    print(result)
    return 0

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
