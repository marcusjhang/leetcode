class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 

        def dfs(grid, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                dfs(grid, row + 1, col)
                dfs(grid, row - 1, col)
                dfs(grid, row, col + 1)
                dfs(grid, row, col - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    islands += 1
                else:
                    continue

        return islands