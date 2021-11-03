class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0  # 0
        cumsum = 0
        remaining = {}  # {7: 2, 8: 2, 10:1}
        for num in nums:  # [3, 4, 3, 4, 6, 8], num = 8
            cumsum += num
            if cumsum == k: # 8 != 4
                res += 1
            if cumsum in remaining: # True
                res += remaining[cumsum] # +2

            remaining[k + cumsum] = remaining.get(k + cumsum, 0) + 1 # 6 + 4 = 10: 1

        return res # 4


if __name__ == '__main__':
    n = [1, 1, 1]
    kk = 2
    print(Solution().subarraySum(n, kk))
