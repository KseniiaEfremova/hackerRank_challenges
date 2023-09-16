def jimOrders(orders):
    # O(nlogn) time
    # O(n) space n - len(serve_time_and_customers)
    # TODO ask len(orders) == len(serve_time_and_customers) in space of memory?
    serve_time_and_customers = []
    for i in range(len(orders[0])):
        serve_time = orders[0][i]+orders[1][i]
        serve_time_and_customers.append((serve_time, i+1))
    serve_time_and_customers.sort()

    return [customer[1] for customer in serve_time_and_customers]


print(jimOrders([[1,2,3], [3,3,3]]))


assert jimOrders([[5,2,3], [1,1,1]]) == [2, 3, 1]
# assert jimOrders([[1,2,3], [1,1,1]]) == [1,2, 3]
# assert jimOrders([[1,2,3], [3,2,1]]) == [1, 2, 3]
# assert jimOrders([[2,2,1], [1,1,1]]) == [3, 1, 2]
# assert jimOrders([[1,2,3], [3,3,3]]) == [1, 2, 3]
# assert jimOrders([[8,4,5,3,4], [1,2,6,1,3]]) == [4,2,5,1,3]
