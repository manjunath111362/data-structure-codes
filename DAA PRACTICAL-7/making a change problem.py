def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[amount] == float('inf'):
        return -1
    else:
        return dp[amount]
n = int(input("Enter number of coins: "))
coins = []
print("Enter coin values:")
for i in range(n):
    coins.append(int(input()))
amount = int(input("Enter amount: "))
result = coin_change(coins, amount)
print("Minimum coins required:", result)
