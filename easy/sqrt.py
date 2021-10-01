class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, 7

        while l < r:
            mid = l + (r - l) // 2
            guess = mid ** 2

            if guess == x:
                return mid
            elif guess < x:
                l = mid + 1
            else:
                r = mid

        return l


if __name__ == '__main__':
    n = 15
    print(Solution().mySqrt(n))
