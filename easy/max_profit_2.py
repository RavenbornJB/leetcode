class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in range(1, len(prices) - 1):
            if prices[i] <= buy:
                buy = prices[i]
            elif prices[i] > buy:
                if prices[i + 1] < prices[i]:
                    profit += prices[i] - buy
                    buy = prices[i + 1]

        profit += max(prices[-1] - buy, 0)
        return profit


if __name__ == '__main__':
    n = [7, 6, 4, 3, 1]
    print(Solution().maxProfit(n))
