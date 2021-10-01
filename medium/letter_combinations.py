class Solution:
    def helper(self, cur, digits, res, dct):
        if len(cur) == len(digits):
            res.append(''.join(cur))
        else:
            for letter in dct[int(digits[len(cur)])]:
                cur.append(letter)
                self.helper(cur, digits, res, dct)
                cur.pop()

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        d = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        res = []
        self.helper([], digits, res, d)

        return res


if __name__ == '__main__':
    s = "23"
    print(Solution().letterCombinations(s))
