import math
import collections


class Solution:
    def combinationSum4(self, candidates: list[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in candidates:
                if num <= i:
                    dp[i] += dp[i - num]

        return dp[-1]


if __name__ == '__main__':
    c = [3, 1, 2, 4]
    t = 4
    print(Solution().combinationSum4(c, t))
