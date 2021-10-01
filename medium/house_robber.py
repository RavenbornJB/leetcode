class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [[0] * len(nums), [0] * len(nums)]
        dp[0][0], dp[1][0] = 0, nums[0]

        for i in range(1, len(nums)):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1])
            dp[1][i] = dp[0][i - 1] + nums[i]

        return max(dp[0][-1], dp[1][-1])


if __name__ == '__main__':
    n = [10, 2, 3, 4, 10]
    print(Solution().rob(n))
