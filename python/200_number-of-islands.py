# DFS with Recursion
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ans = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += self.dfs(grid, i, j)
        return ans


    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return

        grid[i][j] = '0'

        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)

        return 1


#---------------------------------------------------------------------------------------#


# DFS with Stack
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        ans = 0

        stack = collections.deque()


        def dfs(i, j):
            stack.append((i, j))
            while stack:
                x, y = stack.pop()
                if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == '0':
                    continue

                grid[x][y] = '0'
                stack.append((x - 1, y))
                stack.append((x + 1, y))
                stack.append((x, y - 1))
                stack.append((x, y + 1))

            return 1


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += dfs(i, j)

        return ans


#---------------------------------------------------------------------------------------#


# BFS with Queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        ans = 0

        queue = collections.deque()


        def dfs(i, j):
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == '0':
                    continue

                grid[x][y] = '0'
                queue.append((x - 1, y))
                queue.append((x + 1, y))
                queue.append((x, y - 1))
                queue.append((x, y + 1))
            return 1


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += dfs(i, j)

        return ans