from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nxt = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[nxt]:
                nxt += 1
                nums[nxt] = nums[i]
        return nxt + 1


if __name__ == '__main__':
    n = [1, 2, 2, 3]
    print(Solution().removeDuplicates(n), n)
