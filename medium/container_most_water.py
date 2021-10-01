class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_volume = 0

        left, right = 0, len(height) - 1
        while left <= right:
            max_volume = max(max_volume, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_volume


if __name__ == '__main__':
    n = [4, 3, 2, 1, 4]
    print(Solution().maxArea(n))
