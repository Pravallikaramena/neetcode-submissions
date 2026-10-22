
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = [amount + 1] * (amount + 1)
        count[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                count[i] = min(count[i], count[i - coin] + 1)

        if count[amount] <= amount:
            return count[amount]
        else:
            return -1
