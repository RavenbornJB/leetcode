class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)

        cnt = 0
        for stone in stones:
            if stone in jewels:
                cnt += 1

        return cnt


if __name__ == '__main__':
    j = "z"
    s = "ZZ"
    print(Solution().numJewelsInStones(j, s))
