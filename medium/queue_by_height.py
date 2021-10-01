class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        heights = {}

        # first
        available = [person for person in range(len(people)) if people[person][1] == 0]

        if available:
            shortest = min(available, key=lambda x: people[x][0])
            heights[people[shortest][0]] = heights.get(people[shortest][0], 0) + 1

            people[0], people[shortest] = people[shortest], people[0]

        cur = 1
        print(heights)

        return people


if __name__ == '__main__':
    p = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    s = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    print(Solution().reconstructQueue(p))
