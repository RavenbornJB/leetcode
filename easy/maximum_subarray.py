class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        ms = nums[0]
        for num in nums:
            s += num
            ms = max(s, ms)
            s = max(s, 0)
        return ms



if __name__ == '__main__':
    n = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(n))
