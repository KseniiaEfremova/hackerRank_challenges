def flippingBits(n):
    n ^= (1 << 32) - 1
    return n
