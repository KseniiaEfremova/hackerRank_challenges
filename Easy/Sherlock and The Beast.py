def decentNumber(n):
    # O(1) time ?
    # O(n) space, n - len of string
    m = n
    while m % 3 != 0:
        m -= 5

    if m < 0:
        print(-1)
    else:
        print("5" * m, "3"*(n-m), sep="")


print(decentNumber(3))
# assert decentNumber(1) == "-1"
# assert decentNumber(2) == "-1"
# assert decentNumber(3) == "555"
# assert decentNumber(5) == "33333"
# assert decentNumber(8) == "55533333"
# assert decentNumber(16) == "5555553333333333"
# assert decentNumber(15) == "555555555555555"
# assert decentNumber(11) == "55555533333"

