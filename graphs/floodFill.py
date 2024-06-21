class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        visited = set()

        self.dfs(image, sr, sc, image[sr][sc], color, visited)

        return image

    def dfs(self, image, row, col, ori_color, new_color, visited):
        if row < 0 or row == len(image) or col < 0 or col == len(image[0]) or image[row][col] != ori_color or (row, col) in visited:
            return
        
        image[row][col] = new_color
        visited.add((row, col))

        self.dfs(image, row + 1, col, ori_color, new_color, visited)
        self.dfs(image, row -1, col, ori_color, new_color, visited)
        self.dfs(image, row, col + 1, ori_color, new_color, visited)
        self.dfs(image, row, col - 1, ori_color, new_color, visited)

# T O(n) S O(n) -> note: dfs is O(n) because each node is visited once, each visit is O(1)