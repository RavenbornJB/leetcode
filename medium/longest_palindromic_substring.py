class Solution:
    def dp(self, s: str, end):
        if end == 1:
            return 0, 1
        if end == 2 and s[0] == s[1]:
            return 0, 2

        res = self.dp(s, end - 1)
        start = s.find(s[end - 1], 0, end - 1)
        # print(end, res, start)

        while start != -1:
            if end == 12:
                print(s[start:end])
            if end - start < res[1] - res[0]:
                break

            palindrome = True
            for i in range((end - start + 1) // 2):
                if s[start + i] != s[end - 1 - i]:
                    start = s.find(s[end - 1], start + 1, end - 1)
                    palindrome = False
                    break

            if not palindrome:
                continue

            return start, end

        return res

    def longestPalindrome(self, s: str) -> str:
        bounds = self.dp(s, len(s))
        return s[bounds[0]:bounds[1]]


if __name__ == '__main__':
    ss = "ac"
    print(Solution().longestPalindrome(ss))
