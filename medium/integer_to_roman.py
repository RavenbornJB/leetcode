class Solution:
    def intToRoman(self, num: int) -> str:
        d = {(1, 4): "M",
             (5, 3): "D",
             (1, 3): "C",
             (5, 2): "L",
             (1, 2): "X",
             (5, 1): "V",
             (1, 1): "I",
             }
        symbols = []
        num = str(num)
        order = len(num)
        for digit in num:
            cur = int(digit)
            if cur == 9:
                cur -= 9
                symbols += [d[(1, order)], d[(1, order + 1)]]
            if cur == 4:
                cur -= 4
                symbols += [d[(1, order)], d[(5, order)]]
            if cur >= 5:
                cur -= 5
                symbols.append(d[(5, order)])
            if cur > 0:
                symbols += [d[(1, order)] * cur]
            order -= 1

        return ''.join(symbols)


if __name__ == '__main__':
    n = 58
    print(Solution().intToRoman(n))
