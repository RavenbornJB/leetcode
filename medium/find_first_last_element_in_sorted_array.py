class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        first, last = -1, -1

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                r = mid
            else:
                l = mid + 1
        if 0 <= l < len(nums) and nums[l] == target:
            first = l

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                l = mid
            else:
                r = mid - 1
        if 0 <= l < len(nums) and nums[l] == target:
            last = l

        return [first, last]


if __name__ == '__main__':
    n = [4, 4]
    t = 3
    print(Solution().searchRange(n, t))
