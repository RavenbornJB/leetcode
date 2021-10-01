import heapq


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = {}
        for word in words:
            count[word] = count.get(word, 0) - 1

        heap = [(cnt, val) for val, cnt in count.items()]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


if __name__ == '__main__':
    w = ["i","love","leetcode","i","love","coding"]
    k = 2
    print(Solution().topKFrequent(w, k))
