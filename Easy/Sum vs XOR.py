def sumXor(n):
    zero = 0
    while n:
        if n % 2 == 0:
            zero += 1
        n >>= 1

    return 2 ** zero
