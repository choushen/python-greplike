import sys


def match(text, pattern):
    if not pattern:
        print("Pattern is empty")
        return False
    
    if len(pattern) == 1 and pattern in text:
        print(f"Matched single letter '{text}' with pattern: '{pattern}'")
        return True
    
    if pattern[0] == '^':
        print(f"Matched start of line character '{pattern[0]}' - moving to next character")
        return match(pattern[1:], text)
    
    for i in range(len(text) + 1):
        print(f"Trying to match from text position {i}: '{text[i:]}'")
        if match_here(pattern, text[i:]):
            return True
    return False
# match() end

def match_here(text, pattern):
    if not pattern:
        print("Pattern is empty")
        return True
    
    if pattern[0] == '$' and not pattern[1:]:
        print("Matched end of line character")
        return not text
    
    if (text and pattern[0] == '.') or (pattern[0] == text[0]):
        print(f"Matched character '{pattern[0]}' with text '{text[0]}'")
        return match_here(text[1:], pattern[1:])
    
    print(f"Failed to match character '{pattern[0]}' with text '{text[0]}'")
    return False
# match_here() end

def main():
    if len(sys.argv) < 3:
        print("Usage: ./run_pygrep.sh <word> <regex>")
        return
    
    print(f"Matching text: {sys.argv[1]} with pattern: {sys.argv[2]}")
    match(sys.argv[1], sys.argv[2])
# main() end

if __name__ == "__main__":
    main()