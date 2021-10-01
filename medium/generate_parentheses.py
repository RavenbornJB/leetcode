class Solution:
    def transform(self, cur):
        d = {1: '(', -1: ')'}
        return ''.join(map(lambda x: d[x], cur))

    def helper(self, cur, row, res):
        opened = sum(cur)
        if opened < 0:
            return

        if row == len(cur):
            if opened == 0:
                res.append(self.transform(cur))
            return

        cur[row] = 1
        self.helper(cur, row + 1, res)
        cur[row] = -1
        self.helper(cur, row + 1, res)
        cur[row] = 0

    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        thing = [0] * (n * 2)
        self.helper(thing, 0, res)

        return res


if __name__ == '__main__':
    nn = 1
    print(Solution().generateParenthesis(nn))
