class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        res = []

        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        start = 0
        while start < len(s):

            end = s.rindex(s[start])
            i = start

            while i < end:
                end = max(end, last[s[i]])
                i += 1

            res.append(end - start + 1)
            start = end + 1

        return res


if __name__ == '__main__':
    ss = "ababcbacadefegdehijhklij"
    print(Solution().partitionLabels(ss))
