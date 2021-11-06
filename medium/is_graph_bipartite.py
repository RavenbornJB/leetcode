class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        visited = [False] * len(graph)
        colors = [0] * len(graph)
        while not all(visited):
            s = [(visited.index(False), -1)]
            while len(s) > 0:
                node, color = s.pop()
                print(s, node, color)
                if visited[node]:
                    if colors[node] != color:
                        return False
                    continue

                visited[node] = True
                colors[node] = color
                for edge in graph[node]:
                    s.append((edge, color * -1))

        return True


if __name__ == '__main__':
    g = [[1,3],[0,2],[1,3],[0,2]]
    print(Solution().isBipartite(g))
