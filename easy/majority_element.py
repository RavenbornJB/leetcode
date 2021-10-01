from typing import List


class Solution:
    def partMajorityElement(self, nums, start, end):
        if end - start <= 2:
            return nums[start]

        middle = (start + end) // 2
        res_left = self.partMajorityElement(nums, start, middle)
        res_right = self.partMajorityElement(nums, middle, end)
        if res_left == res_right:
            return res_left

        left_count = nums[start:end].count(res_left)
        right_count = nums[start:end].count(res_right)

        if left_count > right_count:
            return res_left
        else:
            return res_right

    def majorityElement(self, nums: List[int]) -> int:
        return self.partMajorityElement(nums, 0, len(nums))

    def partMajorityElement2(self, nums, start):
        candidate = nums[start]
        count = 0
        for i in range(start, len(nums)):
            if nums[i] == candidate:  # IMPROVE
                count += 1
            else:
                count -= 1
            if count == 0:
                return self.partMajorityElement2(nums, i + 1)
        if count > 0:
            return start
        else:
            while nums[start] == candidate:
                start += 1
            return self.partMajorityElement2(nums, start)

    def majorityElement2(self, nums: List[int]) -> int:
        return nums[self.partMajorityElement2(nums, 0)]

    def majorityElement3(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for idx, num in enumerate(nums):
            print(num, candidate, count)
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


if __name__ == '__main__':
    n = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7, 7, 3, 3]
    print(len(n), n.count(7))
    print(Solution().majorityElement3(n))
