class Solution:
    def reverse(self, x: int) -> int:
        top = 2 ** 31 - 1
        bottom = -top - 1

        res = 0
        for digit in reversed(str(abs(x))):
            res = res * 10 + int(digit)

        res *= [-1, 1][x > 0]
        if not bottom <= res <= top:
            return 0
        return res


if __name__ == '__main__':
    n = -15342364
    print(Solution().reverse(n))
