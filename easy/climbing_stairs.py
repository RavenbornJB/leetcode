class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    n = 5
    print(Solution().climbStairs(n))
