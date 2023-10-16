def anagram(s):
    if len(s) % 2 == 1:
        return -1
    first_word = set(s[:len(s)//2])
    second_word = set(s[len(s) // 2:])
    print(first_word)
    print(second_word)
    difference = first_word.difference(second_word)
    print(difference)

    if difference:
        return len(difference)
    else:
        return abs(len(difference) - len(first_word))


print(anagram("abcd"))

# assert anagram("ab") == 1
# assert anagram("bbba") == 1
# assert anagram("abccde") == 2
# assert anagram("aaabbb") == 3
# assert anagram("ab") == 1

