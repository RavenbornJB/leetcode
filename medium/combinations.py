class Solution:
    def combine(self, n: int, k: int, combs=None, cache=None, start=1) -> list[list[int]]:
        if combs is None:
            combs = []
            cache = []

        if k == 1:
            for num in range(start, n + 1):
                combs.append(cache + [num])
        else:
            for num in range(start, n + 1):
                self.combine(n, k - 1, combs, cache + [num], num + 1)

        return combs


if __name__ == '__main__':
    nn = 4
    kk = 2
    print(Solution().combine(nn, kk))
