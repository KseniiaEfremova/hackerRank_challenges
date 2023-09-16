def toys(w):
    # O(nlogn) time
    # O(1) space
    if len(w) == 0:
        return 0
    w.sort()
    count = 0
    min_weight = w[0]
    max_weight = min_weight + 4
    for weight in w:
        if weight > max_weight:
            count += 1
            min_weight = weight
            max_weight = min_weight + 4
    count += 1
    return count


assert toys([]) == 0
assert toys([1]) == 1
assert toys([1,2]) == 1
assert toys([1,5]) == 1
assert toys([1,6]) == 2
assert toys([1,6,11]) == 3
assert toys([1, 2, 3, 21, 7, 12, 14, 21]) == 4
assert toys([10, 2]) == 2
