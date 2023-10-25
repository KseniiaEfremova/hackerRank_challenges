def anagram(s):
    # n - len(s)
    # O(n) time
    # O(n) space
    if len(s) % 2 == 1:
        return -1
    n = len(s) // 2
    first_word = dict()
    second_word = dict()
    res = 0
    for letter in s[:n]:
        first_word[letter] = first_word.get(letter, 0) + 1
    for letter in s[n:]:
        second_word[letter] = second_word.get(letter, 0) + 1
    for letter in first_word:
        if letter in second_word and first_word[letter] > second_word[letter]:
            res += first_word[letter] - second_word[letter]
        elif letter not in second_word:
            res += first_word[letter]
    return res


assert anagram("ab") == 1
assert anagram("bbba") == 1
assert anagram("abccde") == 2
assert anagram("aaabbb") == 3
assert anagram("baaabbba") == 2
assert anagram("aa") == 0
assert anagram("aaaa") == 0
assert anagram("xaxbbbxx") == 1
assert anagram("bbxxxaxb") == 1
