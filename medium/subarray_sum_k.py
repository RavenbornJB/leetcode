class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:  # to do
        count = 0
        d = {}
        for start in range(len(nums)):
            s = 0
            for end in range(start, len(nums)):
                s += nums[end]
                d[s] = d.get(s, 0) + 1
        print(d)
        return count


if __name__ == '__main__':
    n = [1, 1, 1]
    kk = 2
    print(Solution().subarraySum(n, kk))
