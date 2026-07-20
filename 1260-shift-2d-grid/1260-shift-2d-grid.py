class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        result = [[0] * n for _ in range(m)]
        
        k %= total_elements
        
        for r in range(m):
            for c in range(n):
                new_flat_index = (r * n + c + k) % total_elements
                new_r, new_c = divmod(new_flat_index, n)
                result[new_r][new_c] = grid[r][c]
                
        return result