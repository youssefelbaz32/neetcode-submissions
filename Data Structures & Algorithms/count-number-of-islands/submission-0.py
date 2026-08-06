class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        path_set = set()
        def dfs(r, c, path_set): 
            if (r < 0) or (r >= ROWS) or (c < 0) or (c >= COLS) or ((r,c) in path_set) or (grid[r][c] != "1"):
                return
            
            path_set.add((r, c))

            dfs(r + 1, c, path_set)
            dfs(r, c + 1, path_set)
            dfs(r - 1, c, path_set)
            dfs(r, c - 1, path_set)

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in path_set or grid[r][c] != "1":
                    continue
                dfs(r,c, path_set)
                count += 1
        return count
        
            
            

        