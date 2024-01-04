import math


def is_smart_number(num):
    val = int(math.sqrt(num))
    print(val)
    print(val**val)
    if val**2 == num:
        return True
    return False
