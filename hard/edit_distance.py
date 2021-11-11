class Solution:
    def minDistance(self, word1: str, word2: str):
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                cand1 = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    cand1 += 1
                cand2 = dp[i - 1][j] + 1
                cand3 = dp[i][j - 1] + 1
                dp[i][j] = min(cand1, cand2, cand3)

        return dp


# 0 1 2 3
# 1 1 2 3 h
# 2 2 1 2 ho
# 3 2 2 2 hor
# 4 3 3 2 hors
# 5 4 4 3 horse
#   r r r
#     o o
#       s


res = Solution().minDistance("horse", "ros")

for row in res:
    print(' '.join(map(str, row)))
