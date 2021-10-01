class Solution:
    def dfs(self, course):
        self.v[course] = 1
        for c in self.g[course]:
            if self.v[c] == 1:
                return False
            if self.v[c] == 0:
                if not self.dfs(c):
                    return False
        self.v[course] = 2
        return True


    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        self.g = [[] for _ in range(numCourses)]
        for p in prerequisites:
            self.g[p[0]].append(p[1])

        self.v = [0] * numCourses
        for c in range(numCourses):
            if self.v[c] == 0:
                if not self.dfs(c):
                    return False

        return True


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(Solution().canFinish(numCourses, prerequisites))
