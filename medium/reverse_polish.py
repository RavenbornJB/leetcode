class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {"+": int.__add__,
               "-": int.__sub__,
               "*": int.__mul__,
               "/": lambda x, y: int(int.__truediv__(x, y)),
               }
        operands = []
        for token in tokens:
            if token in ops:
                b, a = operands.pop(), operands.pop()
                operands.append(ops[token](a, b))
            else:
                operands.append(int(token))

        return operands[0]


if __name__ == '__main__':
    t = ["1", "-2", "/"]
    print(Solution().evalRPN(t))
