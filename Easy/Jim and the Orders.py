def jimOrders(orders):
    # O(nlogn) time
    # O(n) space n - len(serve_time_and_customers)
    # TODO ask len(orders) == len(serve_time_and_customers) in space of memory?
    serve_time_and_customers = []
    for i in range(len(orders)):
        serve_time = sum(orders[i])
        serve_time_and_customers.append((serve_time, i+1))
    serve_time_and_customers.sort()

    return [customer[1] for customer in serve_time_and_customers]


assert jimOrders([[5,1],[2,1], [3,1]]) == [2, 3, 1]
assert jimOrders([[1,1],[2,1], [3,1]]) == [1,2, 3]
assert jimOrders([[1,3],[2,2], [3,1]]) == [1, 2, 3]
assert jimOrders([[2,1],[2,1], [1,1]]) == [3, 1, 2]
assert jimOrders([[1,3],[2,3], [3,3]]) == [1, 2, 3]
