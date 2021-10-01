class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[n] = nums[n], nums[i]
                n += 1


if __name__ == '__main__':
    n = [0, 1, 0, 3, 12]
    Solution().moveZeroes(n)
    print(n)
