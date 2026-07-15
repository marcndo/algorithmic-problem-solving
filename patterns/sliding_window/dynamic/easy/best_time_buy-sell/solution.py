prices = [10,1,5,6,7,1]

def buy_sell(prices):
    l = 0
    max_profit = 0
    for r in range(len(prices)):
        if prices[l] > prices[r]:
            l = r
        max_profit = max(max_profit, prices[r]-prices[l])
    return max_profit

print(buy_sell(prices))