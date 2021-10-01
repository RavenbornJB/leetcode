class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        for num in nums:
            val = abs(num)
            if nums[val - 1] < 0:
                return val
            else:
                nums[val - 1] *= -1


if __name__ == '__main__':
    n = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(n))
