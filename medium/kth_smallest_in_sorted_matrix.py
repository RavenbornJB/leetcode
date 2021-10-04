import heapq


class Solution:  # O(n * log(n))
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        candidates = [(matrix[i][0], (i, 0)) for i in range(len(matrix))]
        heapq.heapify(candidates)

        val = -69
        for _ in range(k):
            val, pos = heapq.heappop(candidates)
            if pos[1] < len(matrix) - 1:
                heapq.heappush(candidates, (matrix[pos[0]][pos[1] + 1], (pos[0], pos[1] + 1)))

        return val


if __name__ == '__main__':
    #  1  5  9
    # 10 11 13
    # 12 13 15
    m = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    kk = 8
    print(Solution().kthSmallest(m, kk))  # 13
