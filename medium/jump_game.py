class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if reach < i:
                return False
            reach = max(reach, i + nums[i])
        return True


if __name__ == '__main__':
    n = [2, 2, 1, 1, 4]
    print(Solution().canJump(n))
