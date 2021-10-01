import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) - 1

        heap = [(cnt, val) for val, cnt in count.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


if __name__ == '__main__':
    n = [1, 1, 1, 2, 3, 3]
    k = 2
    print(Solution().topKFrequent(n, k))
