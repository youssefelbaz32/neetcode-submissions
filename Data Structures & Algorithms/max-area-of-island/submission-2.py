class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r, c, visited):
            if (r < 0) or (r >= ROWS) or (c < 0) or (c >= COLS) or ((r,c) in visited) or grid[r][c] != 1:
                return 0
            
            visited.add((r,c))

            path1 = dfs(r+1,c,visited)
            path2 = dfs(r-1,c,visited)
            path3 = dfs(r,c+1,visited)
            path4 = dfs(r,c-1,visited)

            return 1 + path1 + path2+ path3 + path4
        

        max_area = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited or grid[r][c] != 1:
                    continue
                area = dfs(r,c,visited)
                if area > max_area:
                    max_area = area

        
        return max_area