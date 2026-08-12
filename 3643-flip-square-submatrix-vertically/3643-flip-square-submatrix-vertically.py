class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            r1, r2 = x + i, x + k - 1 - i
            for j in range(y, y + k):
                grid[r1][j], grid[r2][j] = grid[r2][j], grid[r1][j]
                
        return grid