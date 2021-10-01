import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            diff = abs(heapq.heappop(stones) - heapq.heappop(stones))
            if diff:
                heapq.heappush(stones, -diff)
        return -stones[0] if stones else 0


if __name__ == '__main__':
    s = [5, 8]
    print(Solution().lastStoneWeight(s))
