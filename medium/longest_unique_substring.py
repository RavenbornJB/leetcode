class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 1
        max_len = 0

        while end < len(s):
            pos = s.find(s[end], start, end)
            if pos != -1:
                start = pos + 1
            end += 1
            max_len = max(max_len, end - start)

        return max_len


if __name__ == '__main__':
    st = "kekw"
    print(Solution().lengthOfLongestSubstring(st))
