class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        once = set()
        for num in nums:
            if num not in once:
                once.add(num)
            else:
                once.remove(num)
        return once.pop()


if __name__ == '__main__':
    n = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(n))
