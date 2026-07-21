class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        ans = 0
        mx = 0
        pre = -float('inf')
        i = 0
        
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
                
            cur = j - i
            if s[i] == '1':
                ans += cur
            else:
                mx = max(mx, pre + cur)
                pre = cur
                
            i = j
            
        return ans + mx