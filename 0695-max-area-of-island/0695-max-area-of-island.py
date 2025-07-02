class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        seen = set()
        max_area = 0

        def dfs(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in seen):
                return 0
            seen.add((r,c))
            return (1 + dfs(r + 1,c) + 
                        dfs(r - 1,c) +
                        dfs(r,c + 1) +
                        dfs(r,c - 1))



        for r in range(rows):
            for c in range(cols):               
                max_area = max(max_area, dfs(r,c))

        return max_area
