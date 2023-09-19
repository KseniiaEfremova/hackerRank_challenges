def maximizingXor(l, r):
    # O(?) time
    # O(1) space
    n = l ^ r
    res = 1
    while n:
        res <<= 1
        n >>= 1
    return res - 1
