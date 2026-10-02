class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n < 1:
            return False
        return sorted(nums) == list(range(1, n)) + [n, n]