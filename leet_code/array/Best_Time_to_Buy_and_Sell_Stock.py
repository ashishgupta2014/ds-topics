# single transaction
def maxProfit(array) -> int:
    if len(array) < 2:
        return 0
    buy, sell = 0, 1
    numLength = len(array)
    max_profit = 0
    while sell < numLength:
        if array[sell] > array[buy]:
            profit = array[sell] - array[buy]
            if profit > max_profit:
                max_profit = profit
        else:
            buy = sell

        sell += 1
    return max_profit


# unlimited transactions
def findProfit(array):
    profit = 0
    i = 0
    j = 1
    diff = 0
    n = len(array)-1
    while i <= n:
        if j <= n and array[i] < array[j] and diff < (array[j] - array[i]):
            diff = array[j] - array[i]
            j += 1
        else:
            profit += diff
            i = j
            j += 1
            diff = 0
    return profit


if __name__ == '__main__':
    price = [7, 1, 5, 3, 6, 4]
    print(maxProfit(price))
    print(findProfit(price))
