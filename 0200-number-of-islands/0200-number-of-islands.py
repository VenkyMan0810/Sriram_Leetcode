class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        seen = set()
        island = 0

        def dfs_iterative(r,c):
            stack = [(r,c)]
            while stack:
                row, col = stack.pop()
                if (row, col) in seen:
                    continue
                seen.add((row,col))

                dir = [(1,0), (-1,0), (0,1), (0,-1)]

                for dr, dc in dir:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in seen):
                        stack.append((nr,nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in seen:
                    dfs_iterative(r,c)
                    island += 1

        return island