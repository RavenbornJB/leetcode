class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b = 0
        s = 0
        md = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[s]:
                s = i
            elif prices[i] < prices[b]:
                b = i
                s = i
            md = max(md, prices[s] - prices[b])
        return md


if __name__ == '__main__':
    p = [7, 1, 5, 3, 0, 6, 4]
    print(Solution().maxProfit(p))
