class Solution:
    def combinationSum3(self, k: int, n: int, start=1, combs=None, cache=None) -> list[list[int]]:
        if combs is None:
            combs = []
        if cache is None:
            cache = []

        for num in range(start, 10):
            if num == n and len(cache) == k - 1:
                combs.append(cache + [num])
            if num < n:
                self.combinationSum3(k, n - num, num + 1, combs, cache + [num])

        return combs


if __name__ == '__main__':
    kk = 3
    nn = 9
    print(Solution().combinationSum3(kk, nn))
