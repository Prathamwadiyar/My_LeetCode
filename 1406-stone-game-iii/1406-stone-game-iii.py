class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        a = b = c = 0
        
        for i in range(n - 1, -1, -1):
            ans = stoneValue[i] - a
            if i + 1 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] - b)
            if i + 2 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - c)
            a, b, c = ans, a, b
            
        if a > 0:
            return "Alice"
        elif a < 0:
            return "Bob"
        return "Tie"