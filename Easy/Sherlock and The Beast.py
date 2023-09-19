def decentNumber(n):
    # O(1) time
    # O(1) space
    m = n
    while m % 3 != 0:
        m -= 5

    if m < 0:
        print(-1)
        return

    for i in range(m):
        print(5, end="")
    for i in range(n - m):
        print(3, end="")
    print()


# assert decentNumber(1) == "-1"
# assert decentNumber(2) == "-1"
# assert decentNumber(3) == "555"
# assert decentNumber(5) == "33333"
# assert decentNumber(8) == "55533333"
# assert decentNumber(16) == "5555553333333333"
# assert decentNumber(15) == "555555555555555"
# assert decentNumber(11) == "55555533333"

