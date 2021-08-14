money = int(input())

coin_all = [500,100,50,10]

count = 0

for coin in coin_all:

    if money % coin > 0:

        count = count + (money // coin)

        money = money % coin

    else:

        count = count + (money // coin)

print(count)

