from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        if k == n:
            return max(nums)
            
        if k == 1:
            count = Counter(nums)
            unique_elements = [x for x, freq in count.items() if freq == 1]
            return max(unique_elements) if unique_elements else -1
        count = Counter(nums)
        ans = -1
        
        if count[nums[0]] == 1:
            ans = max(ans, nums[0])
            
        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans