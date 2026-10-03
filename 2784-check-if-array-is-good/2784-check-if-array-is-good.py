class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        nums.sort()
        return nums == list(range(1, n)) + [n, n]