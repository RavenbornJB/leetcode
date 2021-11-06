class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        cur_end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] <= cur_end:
                res[-1][1] = max(cur_end, interval[1])
            else:
                res.append(interval)
            cur_end = res[-1][1]

        return res


if __name__ == '__main__':
    i = [[1, 6], [4, 8], [10, 15], [13, 18], [14, 17]]
    import random
    random.shuffle(i)
    print(Solution().merge(i))
