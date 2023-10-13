def pangrams(s):
    # n - len(s)
    # O(n) time
    # O(n) space
    letters = set()
    for letter in s:
        if letter.isalpha():
            letters.add(letter.lower())
    if len(letters) < 26:
        return "not pangram"
    else:
        return "pangram"


assert pangrams("We promptly judged antique ivory buckles for the prize") == "not pangram"
assert pangrams("We promptly judged antique ivory buckles for the next prize") == "pangram"
assert pangrams("1e promptly judged antique ivory buckles for the next prize") == "not pangram"
assert pangrams("W.e promptly judged antique ivory 3buckles for the next prize") == "pangram"
assert pangrams("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") == "not pangram"
