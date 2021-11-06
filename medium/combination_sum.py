class Solution:
    def combinationSum(self, candidates: list[int], target: int, combs=None, cache=None) -> list[list[int]]:
        if combs is None:
            combs = []
        if cache is None:
            cache = []

        for idx, num in enumerate(candidates):
            if num == target:
                combs.append(cache + [num])
            if num < target:
                self.combinationSum(candidates[idx:], target - num, combs, cache + [num])

        return combs


if __name__ == '__main__':
    c = [2, 3, 6, 7]
    t = 7
    print(Solution().combinationSum(c, t))
