import sys


def match(text, pattern):
    if not pattern:
        print("Pattern is empty")
        return False
    
    if len(pattern) == 1 and pattern in text:
        print(f"Matched single letter{text} with pattern: {pattern}")
        return True
    
    if pattern[0] == '^':
        print(f"Matched start of line {pattern[0]} - moving to next character")
        return match(pattern[1:], text)
    
    # for i in range(len(text) + 1):
    #     print(f"Trying to match from text position {i}: '{text[i:]}'")
    #     if match_here(pattern, text[i:]):
    #         return True
    # return False

    

def main():
    if len(sys.argv) < 3:
        print("Usage: ./run_pygrep.sh <word> <regex>")
        return
    
    print(f"Matching text: {sys.argv[1]} with pattern: {sys.argv[2]}")
    match(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()