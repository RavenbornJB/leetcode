class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for i in range(min(coins), amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                smaller = [coin for coin in coins if coin < i]
                candidates = [dp[i - coin] for coin in smaller if dp[i - coin] > 0]
                if candidates:
                    dp[i] = min(candidates) + 1

        return dp[-1]


if __name__ == '__main__':
    c = [474, 83, 404, 3]
    a = 264
    print(Solution().coinChange(c, a))
