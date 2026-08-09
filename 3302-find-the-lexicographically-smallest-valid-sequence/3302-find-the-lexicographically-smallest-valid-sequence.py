class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        last = [-1] * m
        idx = n - 1
        for j in range(m - 1, -1, -1):
            while idx >= 0 and word1[idx] != word2[j]:
                idx -= 1
            last[j] = idx
            idx -= 1
            
        res = []
        j = 0
        mismatched = False
        
        for i in range(n):
            if j == m:
                break
                
            if not mismatched:
                if j == m - 1 or i < last[j + 1]:
                    res.append(i)
                    if word1[i] != word2[j]:
                        mismatched = True
                    j += 1
                elif word1[i] == word2[j]:
                    res.append(i)
                    j += 1
            else:
                if word1[i] == word2[j] and (j == m - 1 or i < last[j + 1]):
                    res.append(i)
                    j += 1
                    
        return res if len(res) == m else []