from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh_cnt = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh_cnt += 1
                if grid[row][col] == 2:
                    rotten.append([row, col])       

        minutes_passed = 0

        while rotten and fresh_cnt > 0:
            for _ in range(len(rotten)): # this ensures minutes_passed is only incremented once the entire batch of rotten oranges is done
                row, col = rotten.popleft()

                for dx, dy in ([1,0], [-1,0], [0,1], [0,-1]):
                    if (row + dy) < 0 or (row + dy) == len(grid) or (col + dx) < 0 or (col + dx) == len(grid[0]):
                        continue
                    
                    if grid[row + dy][col + dx] != 1:
                        continue
                    
                    else:
                        grid[row + dy][col + dx] = 2
                        rotten.append([row + dy, col + dx])
                        fresh_cnt -= 1

            minutes_passed += 1

        return minutes_passed if fresh_cnt == 0 else -1