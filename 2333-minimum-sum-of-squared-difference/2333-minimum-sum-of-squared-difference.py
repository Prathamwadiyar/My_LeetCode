class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(x - y) for x, y in zip(nums1, nums2)]
        
        if sum(diff) <= k:
            return 0
            
        max_diff = max(diff)
        count = [0] * (max_diff + 1)
        for d in diff:
            count[d] += 1
            
        for d in range(max_diff, 0, -1):
            if count[d] > 0:
                take = min(k, count[d])
                count[d] -= take
                count[d - 1] += take
                k -= take
                if k == 0:
                    break
                    
        return sum(d * d * c for d, c in enumerate(count))