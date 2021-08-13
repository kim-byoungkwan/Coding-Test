def max_profit(prices):

    n = len(prices)

    max_profit = 0

    min_price = prices[0]

    for i in range(1,n):

        profit = prices[i] - min_price

        if profit > max_profit:

            max_profit = profit

        if prices[i] < min_price:

            min_price = prices[i]

    return max_profit


stock = [10700,9600,9800,8200,7800,8300,9500,9800,10400,9500]

print(max_profit(stock))