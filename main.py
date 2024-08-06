import sys


def match(pattern, text):
    if len(pattern) == 1 and pattern in text:
        print("Matched single letter with pattern")
        return True


def main():
    match(sys.argv[1], sys.argv[2])



if __name__ == "__main__":
    main()