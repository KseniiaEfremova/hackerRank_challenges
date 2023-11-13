from itertools import combinations


def alternate(s):
    # n - len(s), m - len(pair_combinations)
    # O(n*m) time
    # O(n) space
    unique_letters = set(s.lower())
    pair_combinations = list(combinations(unique_letters, 2))
    max_lenght = 0
    for pair in pair_combinations:
        cur_letter = ''
        cur_lenght = 0
        for letter in s:
            if letter in pair and letter != cur_letter:
                cur_letter = letter
                cur_lenght += 1
            elif letter in pair and letter == cur_letter:
                cur_lenght = 0
                break
        max_lenght = max(cur_lenght, max_lenght)
    return max_lenght


assert alternate("beabeefeab") == 5
assert alternate("acacaca") == 7
assert alternate("acacacaa") == 0
assert alternate("acdacdacdad") == 8
assert alternate("aaaaaaa") == 0
assert alternate("qwertyuiop") == 2
