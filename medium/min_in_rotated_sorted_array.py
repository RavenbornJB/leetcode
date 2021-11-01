class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            while nums[l] == nums[mid] and l < mid:
                l += 1

            if nums[l] < nums[mid] or l == mid:
                l = mid + 1
            else:
                r = mid

        return nums[l]


#
# 8 0 1 2
# l = 0, r = 1, mid = 1


if __name__ == '__main__':
    n = [1, 0]
    print(Solution().findMin(n))
