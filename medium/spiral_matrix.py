class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:  # nope, don't like, later
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        x, y = 0, 0
        res = []
        while top <= bottom and left <= right:
            while x < right:
                res.append(matrix[y][x])
                x += 1
            top += 1
            while y < bottom:
                res.append(matrix[y][x])
                y += 1
            right -= 1
            while x > left:
                res.append(matrix[y][x])
                x -= 1
            bottom -= 1
            while y > top:
                res.append(matrix[y][x])
                y -= 1
            left += 1

        if top - bottom == 2 and left - right == 2:
            res.append(matrix[y][x])

        return res


if __name__ == '__main__':
    m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(m))
