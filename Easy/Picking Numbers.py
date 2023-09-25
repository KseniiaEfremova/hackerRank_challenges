def pickingNumbers2(a):
    # O(nlogn) time
    # O(1) space
    a.sort()
    left = 0
    right = 0
    longest_subarray = 1
    while right < len(a):
        if a[right] - a[left] <= 1:
            right += 1
        else:
            left += 1
        longest_subarray = max(longest_subarray, right-left)
    return longest_subarray


def pickingNumbers(a):
    # O(n) time
    # O(n) space
    numbers = {}
    for number in a:
        numbers[number] = numbers.get(number, 0) + 1
    longest_subarray = 1
    for key in numbers:
        if key + 1 in numbers:
            longest_subarray = max(numbers[key]+numbers[key+1], longest_subarray)
        else:
            longest_subarray = max(numbers[key], longest_subarray)
    return longest_subarray


print(pickingNumbers([1,1,5,3,3]))
assert pickingNumbers([1,2,2,3,3]) == 4
assert pickingNumbers([1,2,2,2,3]) == 4
assert pickingNumbers([1,1,2,3,3]) == 3
assert pickingNumbers([1,1,5,3,3]) == 2
assert pickingNumbers([1,2,2]) == 3
assert pickingNumbers([1,2]) == 2
assert pickingNumbers([1,1]) == 2
assert pickingNumbers([1,2,2,3,3,3]) == 5