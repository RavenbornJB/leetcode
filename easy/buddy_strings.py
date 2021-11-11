class Solution:
    def buddyStrings(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        same_letters = {}
        diff_idxs = []
        for i in range(len(s1)):
            if s1[i] == s2[i]: # y == y
                same_letters[s1[i]] = same_letters.get(s1[i], 0) + 1
            else:
                diff_idxs.append(i)

        if len(diff_idxs) == 2:
            return s1[diff_idxs[0]] == s2[diff_idxs[1]] and s1[diff_idxs[1]] == s2[diff_idxs[0]]
        elif len(diff_idxs) == 0:
            for value in same_letters.values():
                if value >= 2:
                    return True

        return False
