class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        low, high = min(nums), max(nums)
        
        return [x for x in range(low, high + 1) if x not in num_set]