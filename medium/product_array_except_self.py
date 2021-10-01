class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        left = 1
        right = 1
        for i in range(len(nums)):
            res[i] *= left
            res[-1 - i] *= right

            left *= nums[i]
            right *= nums[-1 - i]

        return res


if __name__ == '__main__':
    n = [-1, 1, 0, -3, 3]
    print(Solution().productExceptSelf(n))
