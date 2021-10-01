from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = -1

        shortest_word = min(map(len, strs))
        for i in range(shortest_word):
            if len(set(map(lambda x: x[i], strs))) != 1:
                break
            idx = i
        return strs[0][:idx + 1]


if __name__ == '__main__':
    s = ["flower", "flow", ""]
    print(Solution().longestCommonPrefix(s))
