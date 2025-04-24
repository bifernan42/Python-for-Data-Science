import sys as sys
from ft_filter import ft_filter


def main(argc, argv):
    """
        My main program function
    """
    sys.tracebacklimit = 0
    assert argc == 3, \
        "the arguments are bad"
    try:
        print(ft_filter(lambda x, y=int(argv[2]): len(x) > y,
                        [word for word in argv[1].split()]))
    except Exception as e:
        print("bad input", e)
    return 0


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
