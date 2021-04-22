import collections

# BFS Solution with Queue
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(i, j):
            queue.append((i, j))
            count = 0
            while queue:
                x, y = queue.popleft()
                if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0:
                    continue

                grid[x][y] = 0
                count += 1
                queue.append((x - 1, y))
                queue.append((x + 1, y))
                queue.append((x, y - 1))
                queue.append((x, y + 1))

            return count


        m = len(grid)  # row
        n = len(grid[0])  # column

        queue = collections.deque()
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = max(count, bfs(i, j))

        return count