import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        res = -69
        for _ in range(k):
            res = heapq.heappop(heap)
        return -res


if __name__ == '__main__':
    n = [3, 2, 1, 5, 6, 4]
    kk = 2
    print(Solution().findKthLargest(n, kk))
