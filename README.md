# python-greplike
Building a greplike pattern matcher in python

Inspired by 'Build your own grep' challenge over at codecrafters

Solution based on the cheatsheet over at https://regexr.com/

## Todo
# Regex Pattern Matcher To-Do List

## Character Classes
- [x] Implement support for `.` (any character except newline)
- [x] Implement support for `\w`, `\d`, `\s` (word, digit, whitespace)
- [x] Implement support for `\W`, `\D`, `\S` (not word, digit, whitespace)
- [x] Implement support for character classes `[abc]` (any of a, b, or c)
- [x] Implement support for negated character classes `[^abc]` (not a, b, or c)
- [ ] Implement support for character ranges `[a-g]` (character between a & g)

## Anchors
- [x] Implement support for `^` (start of the string)
- [x] Implement support for `$` (end of the string)
- [ ] Implement support for `\b` (word boundary)
- [ ] Implement support for `\B` (not-word boundary)

## Escaped Characters
- [ ] Implement support for escaped special characters `\.\*\\`
- [ ] Implement support for escaped whitespace characters `\t`, `\n`, `\r` (tab, linefeed, carriage return)

## Groups & Lookaround
- [ ] Implement support for capture groups `(abc)`
- [ ] Implement support for backreferences `\1` (backreference to group #1)
- [ ] Implement support for non-capturing groups `(?:abc)`
- [ ] Implement support for positive lookahead `(?=abc)`
- [ ] Implement support for negative lookahead `(?!abc)`

## Quantifiers & Alternation
- [ ] Implement support for `*` (0 or more occurrences)
- [ ] Implement support for `+` (1 or more occurrences)
    - [x] Implement support for `+` (1 or more occurrences) for literal characters
    - [ ] Implement support for `+` (1 or more occurrences) for character classes
- [ ] Implement support for `?` (0 or 1 occurrence)
- [ ] Implement support for `{n}` (exactly n occurrences)
- [ ] Implement support for `{n,}` (n or more occurrences)
- [ ] Implement support for `{n,m}` (between n & m occurrences)
- [ ] Implement support for lazy quantifiers `+?`, `{n,}?` (match as few as possible)
- [ ] Implement support for alternation `ab|cd` (match ab or cd)

## Testing & Validation
- [ ] Create unit tests for all implemented features
- [ ] Ensure correct behavior with complex regex patterns
- [ ] Test edge cases and invalid patterns

