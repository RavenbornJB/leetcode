class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0

        prev = 'I'
        for c in s[::-1]:
            if d[c] >= d[prev]:
                res += d[c]
            else:
                res -= d[c]
            prev = c
        return res


if __name__ == '__main__':
    ss = "MCDXLIV"
    print(Solution().romanToInt(ss))
