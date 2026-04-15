"Best time to buy and and sell an item"

def buy_sell(prices):
    i = 0 # when to buy
    profit = 0
    for j in range(1, len(prices)):# j -> when to sell
        if prices[i] >= prices[j]:
            i = j
        profit = max(profit, prices[j] - prices[i])
    return profit

prices = [7, 1, 5, 3, 6, 4]
print(buy_sell(prices))