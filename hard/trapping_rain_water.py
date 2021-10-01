class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []

        water = 0
        for i in range(len(height)):
            while stack and height[i] >= stack[-1][1]:
                idx, bottom = stack.pop()
                if stack:
                    water += (i - stack[-1][0] - 1) * min(height[i] - bottom, stack[-1][1] - bottom)
            stack.append((i, height[i]))

        return water


if __name__ == '__main__':
    h = [1]
    print(Solution().trap(h))
