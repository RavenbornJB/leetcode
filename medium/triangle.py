from copy import deepcopy


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = deepcopy(triangle)

        for i in reversed(range(len(triangle) - 1)):
            for j in range(i + 1):
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])

        return dp[0][0]


if __name__ == '__main__':
    t = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    # t = [[-10]]
    print(t)
    print(Solution().minimumTotal(t))
