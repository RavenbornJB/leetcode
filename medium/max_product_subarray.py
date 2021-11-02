class Solution:
    def maxProduct(self, nums: list[int]) -> int:  # use 2 variables instead of dp, optimizes to O(1) space
        if len(nums) == 1:
            return nums[0]

        dp = [[0, 0] for _ in range(len(nums))]

        if nums[0] < 0:
            dp[0][0] = nums[0]
            dp[0][1] = 0
        else:
            dp[0][0] = 0
            dp[0][1] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                dp[i][0] = dp[i - 1][1] * nums[i] if dp[i - 1][1] else nums[i]
                dp[i][1] = dp[i - 1][0] * nums[i] if dp[i - 1][0] else dp[i - 1][0]
            else:
                dp[i][0] = dp[i - 1][0] * nums[i] if dp[i - 1][0] else dp[i - 1][0]
                dp[i][1] = dp[i - 1][1] * nums[i] if dp[i - 1][1] else nums[i]

        return max(arr[1] for arr in dp)


# -10 5 -3 -4
# [-10, None] [-50, 5], [-15, 150], [-600, 60]

# 10 -3 -4
# [10] [-30, -3] [120]


if __name__ == '__main__':
    n = [-2]
    print(Solution().maxProduct(n))
