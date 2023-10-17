def anagram(s):
    # O(n) time
    # O(n) space
    if len(s) % 2 == 1:
        return -1
    n = len(s)//2
    first_word = list(s[:n])
    second_word = list(s[n:])
    for letter in first_word:
        if letter in second_word:
            second_word.remove(letter)
    return len(second_word)


assert anagram("ab") == 1
assert anagram("bbba") == 1
assert anagram("abccde") == 2
assert anagram("aaabbb") == 3
assert anagram("baaabbba") == 2
assert anagram("aa") == 0
assert anagram("aaaa") == 0
assert anagram("xaxbbbxx") == 1
assert anagram("bbxxxaxb") == 1
