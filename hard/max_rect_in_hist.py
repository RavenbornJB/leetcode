class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        width = [1] * len(heights)
        lstack = []
        rstack = []

        for i in range(len(heights)):
            while lstack and heights[i] < heights[lstack[-1]]:
                width[lstack[-1]] += i - lstack.pop() - 1
            lstack.append(i)

        for i in range(len(heights) - 1, -1, -1):
            while rstack and heights[i] < heights[rstack[-1]]:
                width[rstack[-1]] += rstack.pop() - i - 1
            rstack.append(i)

        for i in lstack:
            width[i] += len(heights) - i - 1

        for i in rstack:
            width[i] += i

        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i] * width[i])

        return max_area

# start     [2, 1, 5, 6, 2, 3]
# l         [0, 4, 1, 0, 1, 0]
# r         [0, 1, 0, 0, 2, 0]
# sum + 1   [1, 6, 2, 1, 4, 1]
# * val     [2, 6, 10, 6, 8, 3]


if __name__ == '__main__':
    h = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(h))
