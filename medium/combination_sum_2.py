class Solution:
    def combinationSum2(self, candidates: list[int], target: int, combs=None, cache=None) -> list[list[int]]:
        if combs is None:
            combs = []
            candidates.sort()
        if cache is None:
            cache = []

        prev_num = 0
        for idx, num in enumerate(candidates):
            if num == prev_num:
                continue
            prev_num = num
            if num == target:
                combs.append(cache + [num])
            if num < target:
                combs = self.combinationSum2(candidates[idx + 1:], target - num, combs, cache + [num])

        return combs


if __name__ == '__main__':
    c = [10, 1, 2, 7, 6, 1, 5]
    t = 8
    print(Solution().combinationSum2(c, t))
