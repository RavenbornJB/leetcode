class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort() # [1, 3, 5]

        max_length = 1

        print(nums)
        start = nums[0]
        prev = nums[0]
        for el in nums[1:]:
            if el - prev > 1:
                max_length = max(max_length, prev - start + 1)
                start = el
            prev = el

        max_length = max(max_length, nums[-1] - start + 1)

        return max_length

    def longestConsecutive2(self, nums: list[int]) -> int:
        max_length = 0
        nums = set(nums)
        for el in nums:
            if el - 1 not in nums:
                length = 1
                while el + length in nums:
                    length += 1
                max_length = max(max_length, length)

        return max_length


if __name__ == '__main__':
    n = [0, 1, 1, 2]
    print(Solution().longestConsecutive2(n))
