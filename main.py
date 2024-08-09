# import sys
from typing import Union, Dict


class PatternMatcher:

    original_text: str  = ""
    original_pattern: str = ""
    capture_groups: Dict[str, str] = {}

    def match(self, text: str, pattern: str) -> Union[bool, None]:
        self.original_text = text
        self.original_pattern = pattern

        if not pattern:
            print("Pattern is empty")
            return False
        
        if len(pattern) == 1 and pattern in text:
            print(f"Matched single letter '{text}' with pattern: '{pattern}'")
            return True
        
        if pattern[0] == '^':
            print(f"Matched start of line character '{pattern[0]}' - moving to next character")
            return self.match(text, pattern[1:])
        
        for i in range(len(text) + 1):
            print(f"Trying to match from text position {i}: '{text[i:]}'")
            if self.match_here(text, pattern):
                return True
        return False
    # match() end


    def match_here(self, text: str, pattern: str) -> Union[bool, None]:
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
            return self.match_here(text[1:], pattern[1:])
        
        if pattern[0] == '\\':
            print(f'meow {pattern}')
            return self.match_type(text, pattern[1:])
        
        if pattern[0] == '[':
            if pattern[1] == '^':
                print(f"Matched character set negation '{pattern[1]}'")
                return self.match_set(self.original_text, text, pattern[2:])
            else:
                print(f"Matched character set '{pattern[0]}'")
                return self.match_set(self.original_text, text, pattern[1:])

                
        
        print(f"Failed to match character '{pattern[0]}' with text '{text[0]}'")
        return False
    # match_here() end


    def match_set(self, original_text: str, text: str, pattern: str) -> Union[bool, None]:
            set_part, rest = pattern.split(']', 1)
            if any(char in original_text for char in set_part):
                return self.match_here(text, rest)
            return False
    

    
    '''
    Create a 'match_type' that handles cases for \\w, \\d, \\s, etc.
    '''
    def match_type(self, text, pattern) -> Union[bool, None]:
        print(f"Matched escape character so entering match_type: currently at  {pattern[0]} and {text[0]}")
        if pattern[0] == 'w' and text[0].isalnum() or text[0] == '_':
            print(f"Matched word character '{text[0]}' with pattern '{pattern[0]}'")
            return self.match_here(text[1:], pattern[1:])

        if pattern[0] == 'd' and text[0].isdigit():
            print(f"Matched digit character '{text[0]}' with pattern '{pattern[0]}'")
            return self.match_here(text[1:], pattern[1:])

        if pattern[0] == 's' and text[0].isspace():
            print(f"Matched whitespace character '{text[0]}' with pattern '{pattern[0]}'")
            return self.match_here(text[1:], pattern[1:])
        
        if pattern[0] == 'W' and not text[0].isalnum():
            print(f"Matched a none word character '{text[0]}' with pattern '{pattern[0]}'")
            return self.match_here(text[1:], pattern[1:])

        if pattern[0] == 'D' and not text[0].isdigit():
            print(f"Matched a none digit character '{text[0]}' with pattern '{pattern[0]}'")
            return self.match_here(text[1:], pattern[1:])

        if pattern[0] == 'S' and not text[0].isspace():
            print(f"Matched a none whitespace character '{text[0]}' with pattern '{pattern[0]}'")
            return self.match_here(text[1:], pattern[1:])
        
        return False

# PatternMatcher() end


def main() -> None:
    matcher = PatternMatcher()
    matcher.match("abc2a", "^a\\wc\\d[abc]\\w+")

    # if len(sys.argv) < 3:
    #     print("Usage: ./run_pygrep.sh <word> <regex>")
    #     return
    
    # print(f"Matching text: {sys.argv[1]} with pattern: {sys.argv[2]}")
    # match(sys.argv[1], sys.argv[2])
    # match('abc2', '^a\\wc\\d[abc]')
# main() end

if __name__ == "__main__":
    main()