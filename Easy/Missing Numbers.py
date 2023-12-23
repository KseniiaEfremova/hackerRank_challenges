def missingNumbers(arr, brr):
    # TC O(n), n - len(brr)
    # SC O(n), n - len(brr)
    numbers = {}
    for number in brr:
        numbers[number] = numbers.get(number, 0) + 1
    for number in arr:
        numbers[number] = numbers.get(number, 0) - 1
    res = {n for n in brr if numbers[n] > 0}
    return sorted(res)


assert missingNumbers([1,2,2,3], [1,1,2,2,3,3]) == [1,3]
assert missingNumbers([203, 204, 205, 206, 207, 208, 203, 204, 205, 206], [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]) == [204, 205, 206]