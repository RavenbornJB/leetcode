class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    n = [1, 3, 5, 6]
    t = 0
    print(Solution().searchInsert(n, t))
