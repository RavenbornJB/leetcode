class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            rows.append([0] * (i + 1))
            rows[-1][0] = 1
            rows[-1][-1] = 1
            for j in range(1, i):
                rows[-1][j] = rows[-2][j - 1] + rows[-2][j]

        return rows


print(Solution().generate(5))
