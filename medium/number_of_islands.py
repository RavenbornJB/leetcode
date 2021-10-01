class Solution:
    def dfs(self, grid, h, w):
        s = [(h, w)]

        while s:
            i, j = s.pop()
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                continue
            grid[i][j] = "0"
            s.append((i + 1, j))
            s.append((i - 1, j))
            s.append((i, j + 1))
            s.append((i, j - 1))

    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    self.dfs(grid, i, j)
        return islands


if __name__ == '__main__':
    g = [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "1", "1", "1"]
    ]
    print(Solution().numIslands(g))
