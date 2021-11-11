class Solution:
    def skip_backspaces(self, s, idx):
        backspaces = 2 * int(s[idx] == "#")
        while backspaces > 0:
            idx -= 1
            if idx >= 0 and s[idx] == "#":
                backspaces += 1
            else:
                backspaces -= 1
        return idx

    def backspaceCompare(self, s1: str, s2: str) -> bool:
        i1, i2 = len(s1) - 1, len(s2) - 1  # -1, -1

        while i1 >= 0 and i2 >= 0:  # True
            i1 = self.skip_backspaces(s1, i1)
            i2 = self.skip_backspaces(s2, i2)
            if i1 < 0 or i2 < 0:
                break
            elif s1[i1] != s2[i2]:  # a == a
                return False
            i1 -= 1
            i2 -= 1

        while i1 >= 0:
            if s1[i1] != "#":
                return False
            i1 = self.skip_backspaces(s1, i1)

        while i2 >= 0:
            if s2[i2] != "#":
                return False
            i2 = self.skip_backspaces(s2, i2)

        return True


if __name__ == '__main__':
    ss1 = "nzp#o#g"
    ss2 = "b#nzp#o#g"
    print(Solution().backspaceCompare(ss1, ss2))
