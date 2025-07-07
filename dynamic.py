def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    # Масив для мінімальної кількості монет
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Масив для відновлення рішення
    prev = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    # Відновлення кількості монет
    result = {}
    i = amount
    while i > 0:
        coin = prev[i]
        result[coin] = result.get(coin, 0) + 1
        i -= coin

    return result
 
print(find_min_coins(113, coins=[50, 25, 10, 5, 2, 1]))