from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i, num in enumerate(nums) if num > 0]


if __name__ == '__main__':
    n = [1, 3, 4, 3]
    print(Solution().findDisappearedNumbers(n))
