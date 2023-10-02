def theGreatXor(x):
    count = 0
    for a in range(x):
        if a ^ x > x > a > 0:
            count += 1
    return count


print("result ", theGreatXor(5))

assert theGreatXor(5) == 2
assert theGreatXor(2) == 1
assert theGreatXor(10) == 5
assert theGreatXor(100) == 27
assert theGreatXor(5) == 2
