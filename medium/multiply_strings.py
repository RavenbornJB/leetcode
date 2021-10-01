class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        for c1 in range(len(num1)):
            for c2 in range(len(num2)):
                prod = str(int(num1[-1 - c1]) * int(num2[-1 - c2]) * 10**(c1 + c2))
                for c in range(len(prod)):
                    res[-1 - c] += int(prod[-1 - c])
                    chain = 0
                    while res[-1 - c - chain] >= 10:
                        res[-1 - c - chain] -= 10
                        res[-2 - c - chain] += 1
                        chain += 1

        start = 0
        while start < len(res) - 1 and res[start] == 0:
            start += 1
        return ''.join(map(str, res[start:]))


if __name__ == '__main__':
    n1 = "0"
    n2 = "0"
    print(Solution().multiply(n1, n2))
