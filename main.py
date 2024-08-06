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
        return match(text, pattern[1:])
    
    for i in range(len(text) + 1):
        print(f"Trying to match from text position {i}: '{text[i:]}'")
        if match_here(text, pattern):
            return True
    return False
# match() end


def match_here(text, pattern):
    print(f'match_here: text: {text} and pattern: {pattern}')

    # If pattern is empty, return True because we have matched all characters
    if not pattern:
        print("Pattern is empty")
        return True
    #print current index of text and pattern
    print(f"Current text index: {text[0]} and pattern index: {pattern[0]}")

   # Matched end of line character 
    if pattern[0] == '$' and not pattern[1:]:
        print("Matched end of line character")
        return not text
    
    # Literal match
    if (text and pattern[0] == '.') or (pattern[0] == text[0]):
        print(f"Matched character '{pattern[0]}' with text '{text[0]}'")
        return match_here(text[1:], pattern[1:])
    
    if pattern[0] == '\\':
        print(f'meow {pattern}')
        return match_type(text, pattern[1:])
    
    print(f"Failed to match character '{pattern[0]}' with text '{text[0]}'")
    return False
# match_here() end

'''
Create a 'match_type' that handles cases for \\w, \\d, \\s, etc.
and within that, i will handle cases for +, *, ?, etc.
'''
def match_type(text, pattern):
    print(f"Matched escape character so entering match_type: currently at  {pattern[0]} and {text[0]}")
    if pattern[0] == 'w' and text[0].isalnum():
        print(f"Matched word character '{text[0]}' with pattern '{pattern[0]}'")
        return match_here(text[1:], pattern[1:]) 

def main():
    # if len(sys.argv) < 3:
    #     print("Usage: ./run_pygrep.sh <word> <regex>")
    #     return
    
    # print(f"Matching text: {sys.argv[1]} with pattern: {sys.argv[2]}")
    # match(sys.argv[1], sys.argv[2])
    print("Matching text: abc with pattern: a\\wc")
    match('abc', '^a\\wc')
# main() end

if __name__ == "__main__":
    main()