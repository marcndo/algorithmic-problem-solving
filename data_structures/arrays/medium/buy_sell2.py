def max_profit1(prices):
    j = 0
    total = 0
    for i in range(1, len(prices)):
        profit = prices[i] - prices[j]
        if profit < 0:
            j = i
        else:
            total += profit
            j += 1
    return total