from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        letters = Counter(p)
        res = []

        word_start = -1
        count = letters.copy()

        for i, c in enumerate(s):
            if c in letters:
                if word_start == -1:
                    word_start = i
                elif i >= word_start + len(p):
                    count[s[word_start]] += 1
                    word_start += 1
                count[c] -= 1
                if not any(count.values()):
                    res.append(word_start)

            elif word_start != -1:
                count = letters.copy()
                word_start = -1

        return res


if __name__ == '__main__':
    ss = "cbaebabacd"
    pp = "abc"
    print(Solution().findAnagrams(ss, pp))
