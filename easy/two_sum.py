class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target - nums[i] in nums:
                j = nums.index(target - nums[i])
                if j != -1 and i != j:
                    return [i, j]


if __name__ == '__main__':
    n = [2, 7, 11, 15]
    o = 9
    print(Solution().twoSum(n, o))
