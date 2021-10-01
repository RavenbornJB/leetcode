class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(n)]
        for _ in range(m - 1):
            for i in range(1, n):
                row[i] += row[i - 1]
        return row[-1]


if __name__ == '__main__':
    m, n = 1, 1
    print(Solution().uniquePaths(m, n))
