class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
            
        if xor_sum != 0:
            return len(nums)
            
        for num in nums:
            if num > 0:
                return len(nums) - 1
                
        return 0