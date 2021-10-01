from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = Counter(t)
        queue = []

        res = len(s)
        p1 = mp1 = 0
        p2 = mp2 = 0

        while p2 < len(s):
            p2 += 1
            char = s[p2 - 1]

            if char in chars:
                queue.append((char, p2 - 1))
                p1 = queue[0][1]
                chars[char] -= 1

            while len(queue) > 0 and chars[queue[0][0]] < 0:
                chars[queue[0][0]] += 1
                queue.pop(0)
                if queue:
                    p1 = queue[0][1]

            if all(map(lambda x: x <= 0, chars.values())) and p2 - p1 <= res:
                mp1, mp2 = p1, p2
                res = p2 - p1
            # print(s[p1:p2], (mp1, mp2), chars, queue)

        return s[mp1:mp2]


if __name__ == '__main__':
    ss = "ADOBECODEBANC"
    tt = "ABCC"
    print(Solution().minWindow(ss, tt))
