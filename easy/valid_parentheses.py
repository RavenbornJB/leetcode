class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in d:
                stack.append(c)
            elif len(stack) > 0 and stack[-1] == d[c]:
                stack.pop()
            else:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    s = "([]){}"
    print(Solution().isValid(s))
