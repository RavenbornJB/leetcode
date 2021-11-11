class Solution:
    def numSquares(self, n: int) -> int:
        coins = [(i + 1) ** 2 for i in range(int(n ** 0.5))]
        dp = [-1] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            if i in coins:
                dp[i] = 1
            else:
                smaller = [dp[i - coin] for coin in coins if coin < i]
                if smaller:
                    dp[i] = min(smaller) + 1

        return dp[-1]
